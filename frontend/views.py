"""Frontend-only views for the IoT Lab Inventory Management System.

Backend note:
These views intentionally render templates with little or no database context.
The backend team can replace the placeholder context with models, forms, and
permission checks later without changing the template names or URL names.
"""

from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.shortcuts import redirect, render

from .user_helpers import (
    apply_role,
    build_dashboard_user,
    normalize_role,
    split_full_name,
    username_from_email,
)


def login_page(request):
    """Render the login page."""
    return render(request, "accounts/login.html")


def register_page(request):
    """Render the registration page."""
    return render(request, "accounts/register.html")


def forgot_password_page(request):
    """Render the password reset placeholder page."""
    return render(request, "accounts/forgot_password.html")


def profile(request):
    """Render the user profile page."""
    return render(request, "accounts/profile.html")


def dashboard(request):
    """Render the student dashboard page."""
    return render(request, "user/dashboard.html")


def inventory_list(request):
    """Render the inventory browser page."""
    return render(request, "user/inventory_list.html")


def item_detail(request, item_id):
    """Render an item detail page.

    Backend expected later: fetch the item by item_id and pass it as "item".
    """
    context = {"item": {"id": item_id}}
    return render(request, "user/item_detail.html", context)


def borrow_request(request):
    """Render the borrow request form page."""
    selected_item_id = request.GET.get("item")
    return render(request, "user/borrow_request.html", {"selected_item_id": selected_item_id})


def reservation_list(request):
    """Render the current user's reservation list."""
    return render(request, "user/reservation_list.html")


def my_borrowings(request):
    """Render the current user's borrowing list."""
    return render(request, "user/my_borrowings.html")


def lost_report(request):
    """Render the lost item report form."""
    return render(request, "user/lost_report.html")


def admin_dashboard(request):
    """Render the frontend admin dashboard."""
    return render(request, "admin_ui/admin_dashboard.html")


def item_manage(request):
    """Render the admin item management page."""
    return render(request, "admin_ui/item_manage.html")


def item_form(request, item_id=None):
    """Render the add/edit item form.

    Backend expected later: if item_id is provided, fetch and pass "item".
    """
    context = {"item": {"id": item_id}} if item_id else {}
    return render(request, "admin_ui/item_form.html", context)


def borrow_requests(request):
    """Render the admin borrow request review page."""
    return render(request, "admin_ui/borrow_requests.html")


def user_manage(request):
    """Render and process the admin user management page.

    Backend note:
    This uses Django's built-in auth_user table in the existing SQLite database.
    If the backend team later adds a profile/student model, keep this view and
    frontend/user_helpers.py as the integration points for dashboard user create.
    """
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "create_user":
            full_name = request.POST.get("full_name", "").strip()
            email = request.POST.get("email", "").strip().lower()
            role = normalize_role(request.POST.get("role", ""))

            if not full_name or not email:
                messages.error(request, "Full name and email are required to add a user.")
                return redirect("user_manage")

            if (
                User.objects.filter(email__iexact=email).exists()
                or User.objects.filter(username__iexact=username_from_email(email)).exists()
            ):
                messages.error(request, "A user with this email already exists.")
                return redirect("user_manage")

            first_name, last_name = split_full_name(full_name)

            try:
                with transaction.atomic():
                    user = User.objects.create_user(
                        username=username_from_email(email),
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.set_unusable_password()
                    apply_role(user, role)
                messages.success(request, f"{full_name} was added as {role}.")
            except IntegrityError:
                messages.error(request, "A user with this email already exists.")

            return redirect("user_manage")

        if action == "remove_user":
            user_id = request.POST.get("user_id")
            deleted_count, _ = User.objects.filter(id=user_id).delete()
            if deleted_count:
                messages.success(request, "User account removed.")
            else:
                messages.error(request, "User account could not be found.")
            return redirect("user_manage")

        if action == "view_activity":
            messages.info(request, "Borrowing activity can be connected here when backend borrowing models are ready.")
            return redirect("user_manage")

    users = [build_dashboard_user(user) for user in User.objects.order_by("first_name", "last_name", "username")]
    return render(request, "admin_ui/user_manage.html", {"users": users})


def reports(request):
    """Render the admin reports page."""
    return render(request, "admin_ui/reports.html")
