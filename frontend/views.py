"""Frontend-only views for the IoT Lab Inventory Management System.

Backend note:
These views intentionally render templates with little or no database context.
The backend team can replace the placeholder context with models, forms, and
permission checks later without changing the template names or URL names.
"""

from django.shortcuts import render


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
    """Render the admin user management page."""
    return render(request, "admin_ui/user_manage.html")


def reports(request):
    """Render the admin reports page."""
    return render(request, "admin_ui/reports.html")
