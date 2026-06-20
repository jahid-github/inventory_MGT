"""Frontend URL routes for the IoT Lab Inventory template scaffold.

Backend note:
Keep these URL names stable because templates already use them with {% url %}.
Views can later be replaced with model-backed class-based or function views.
"""

from django.urls import path

from . import views


urlpatterns = [
    # Account pages.
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("forgot-password/", views.forgot_password_page, name="forgot_password"),
    path("profile/", views.profile, name="profile"),

    # Student pages.
    path("", views.dashboard, name="user_dashboard"),
    path("dashboard/", views.dashboard),
    path("inventory/", views.inventory_list, name="inventory_list"),
    path("inventory/<int:item_id>/", views.item_detail, name="item_detail"),
    path("borrow-request/", views.borrow_request, name="borrow_request"),
    path("reservations/", views.reservation_list, name="reservation_list"),
    path("my-borrowings/", views.my_borrowings, name="my_borrowings"),
    path("lost-report/", views.lost_report, name="lost_report"),

    # Admin UI pages. These are frontend routes, not Django admin routes.
    path("admin-ui/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-ui/items/", views.item_manage, name="item_manage"),
    path("admin-ui/items/new/", views.item_form, name="item_create"),
    path("admin-ui/items/<int:item_id>/edit/", views.item_form, name="item_edit"),
    path("admin-ui/borrow-requests/", views.borrow_requests, name="borrow_requests"),
    path("admin-ui/users/", views.user_manage, name="user_manage"),
    path("admin-ui/reports/", views.reports, name="reports"),
]
