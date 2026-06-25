"""Shared helpers for creating inventory users from admin entry points."""

from django.contrib.auth.models import Group, User


ROLE_STUDENT = "Student"
ROLE_TEACHER = "Teacher"
ROLE_ADMIN = "Admin"
ROLE_CHOICES = (ROLE_STUDENT, ROLE_TEACHER, ROLE_ADMIN)


def normalize_role(role):
    """Return a supported display role, defaulting to the safest user access."""
    return role if role in ROLE_CHOICES else ROLE_STUDENT


def split_full_name(full_name):
    """Split a single dashboard name field into Django's first/last name fields."""
    parts = full_name.strip().split(maxsplit=1)
    first_name = parts[0] if parts else ""
    last_name = parts[1] if len(parts) > 1 else ""
    return first_name, last_name


def username_from_email(email):
    """Use email as the username so both admin entry points share one login key."""
    return email.strip().lower()


def display_role(user):
    """Map Django auth flags back to the role labels used by the admin dashboard."""
    if user.is_superuser:
        return ROLE_ADMIN
    if user.is_staff:
        return ROLE_TEACHER
    return ROLE_STUDENT


def apply_role(user, role, commit=True):
    """Apply dashboard role semantics to Django auth fields.

    Backend note:
    This intentionally keeps role storage on Django's built-in User table and
    auth groups. If a profile model is added later, update this helper first so
    the custom dashboard and Django Administration continue to behave the same.
    """
    role = normalize_role(role)
    user.is_staff = role in (ROLE_TEACHER, ROLE_ADMIN)
    user.is_superuser = role == ROLE_ADMIN

    if commit:
        user.save()
        for group_name in ROLE_CHOICES:
            group, _ = Group.objects.get_or_create(name=group_name)
            if group_name == role:
                user.groups.add(group)
            else:
                user.groups.remove(group)
    return user


def build_dashboard_user(user):
    """Return the shape expected by templates/admin_ui/user_manage.html."""
    full_name = user.get_full_name().strip() or user.username
    return {
        "id": user.id,
        "full_name": full_name,
        "email": user.email,
        "student_id": "",
        "role": display_role(user),
        "active_borrowings": 0,
    }
