from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


admin.site.unregister(User)


class InventoryUserCreationForm(UserCreationForm):
    """Django Administration form that mirrors the custom admin dashboard."""

    role = forms.ChoiceField(
        choices=(("Student", "Student"), ("Teacher", "Teacher"), ("Admin", "Admin")),
        initial="Student",
        help_text="Matches the role options used in the custom admin dashboard.",
    )
    admin_note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
        help_text="Backend note placeholder; add a profile/audit model later if this must be stored.",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name", "role")

    def save(self, commit=True):
        from .user_helpers import apply_role

        user = super().save(commit=False)
        if commit:
            user.save()
            apply_role(user, self.cleaned_data["role"])
        return user


@admin.register(User)
class InventoryUserAdmin(DjangoUserAdmin):
    """User admin customized for the inventory project's user roles.

    Backend note:
    Both /admin-ui/users/ and Django Administration use the same SQLite-backed
    auth_user table. If a custom user/profile model is introduced later, migrate
    this admin class together with frontend.views.user_manage.
    """

    add_form = InventoryUserCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "role",
                    "admin_note",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "inventory_role", "is_active")
    list_filter = ("is_active", "is_staff", "is_superuser", "groups")

    @admin.display(description="Role")
    def inventory_role(self, user):
        from .user_helpers import display_role

        return display_role(user)
