<!--
  Frontend handoff notes for the IoT Lab Inventory Management System.
  Backend developers can use this file to connect Django views, forms, permissions, and PostgreSQL data.
-->

# IoT Lab Inventory Frontend

This folder contains a Django-template frontend scaffold for the IoT Lab Inventory Management System. It is intentionally model-light: templates use clear context names, empty states, and placeholder controls so backend work can connect real data later.

## Template Map

- `templates/base.html`: Shared application shell with `{% block title %}`, `{% block extra_css %}`, `{% block content %}`, and `{% block extra_js %}`.
- `templates/components/navbar.html`: Logged-in top navigation with project name, search, notifications, profile menu, and dark mode toggle.
- `templates/components/sidebar.html`: Student and admin navigation links. Backend can hide admin links by role.
- `templates/components/footer.html`: Shared footer.
- `templates/components/status_badge.html`: Reusable status badge include. Pass `status`.
- `templates/components/alert_messages.html`: Django messages placeholder.
- `templates/accounts/login.html`: Login form.
- `templates/accounts/register.html`: Student registration form.
- `templates/accounts/forgot_password.html`: Password reset request placeholder.
- `templates/accounts/profile.html`: User profile and borrowing summary.
- `templates/user/dashboard.html`: Student statistics, recent activity, quick actions, and Chart.js placeholder.
- `templates/user/inventory_list.html`: Searchable/filterable inventory cards.
- `templates/user/item_detail.html`: Item detail, QR placeholder, and borrowing history.
- `templates/user/borrow_request.html`: Borrow request form.
- `templates/user/reservation_list.html`: User reservation table.
- `templates/user/my_borrowings.html`: Current borrowed items and overdue badge display.
- `templates/user/lost_report.html`: Lost item report form.
- `templates/admin_ui/admin_dashboard.html`: Admin statistics, recent requests, lost reports, and chart placeholder.
- `templates/admin_ui/item_manage.html`: Admin item table with search/filter.
- `templates/admin_ui/item_form.html`: Add/edit item form.
- `templates/admin_ui/borrow_requests.html`: Request review table.
- `templates/admin_ui/user_manage.html`: User management table.
- `templates/admin_ui/reports.html`: Lost and overdue item reports.

## CSS Files

- `static/css/base.css`: Global layout, theme variables, navbar, sidebar, buttons, forms, tables, alerts, badges, responsive behavior, and dark mode.
- `static/css/auth.css`: Login, register, and password reset pages.
- `static/css/dashboard.css`: Dashboard cards, chart panels, profile layout, and reports grids.
- `static/css/inventory.css`: Inventory cards, detail page, QR area, and item forms.

## JavaScript Files

- `static/js/main.js`: Mobile sidebar, profile dropdown, dark mode with `localStorage`, and submit-button loading states.
- `static/js/dashboard_charts.js`: Demo Chart.js charts. Backend can set `window.dashboardChartData` before loading this file.
- `static/js/inventory_filter.js`: Frontend-only filtering for elements with `data-inventory-card`.
- `static/js/qr_scanner.js`: Placeholder QR scanner behavior. Add `html5-qrcode` initialization here later.

## Expected Backend Context

Use these context names when wiring Django views:

- `stats`: `{total_items, available_items, borrowed_items, pending_requests}`
- `admin_stats`: `{total_assets, available_assets, open_requests, overdue_items}`
- `items`: list/queryset with `id`, `name`, `category`, `serial_number`, `location`, `status`, `description`, and optional `image_url`
- `categories`: list of category names for filter selects
- `recent_activities`: list with `title`, `item_name`, `status`, `created_at`
- `borrowing_history`: list with `borrower_name`, `borrowed_at`, `returned_at`, `status`
- `reservations`: list with `item_name`, `reserved_from`, `reserved_to`, `status`, `id`
- `borrowings`: list with `item_name`, `borrowed_at`, `expected_return_date`, `status`, `is_overdue`, `id`
- `borrowed_items`: list of currently borrowed items for lost report selection
- `recent_requests` or `requests`: list with `requester_name`, `item_name`, `borrow_date`, `expected_return_date`, `reason`, `status`
- `lost_reports`: list with `item_name`, `reported_by`, `location_lost`, `date_lost`, `status`
- `overdue_items`: list with `item_name`, `borrower_name`, `expected_return_date`, `days_late`
- `users`: list with `full_name`, `email`, `student_id`, `role`, `active_borrowings`
- `borrowing_summary`: `{current, returned, pending, overdue}`

## URL Names

Templates use these Django URL names:

- `login`
- `register`
- `profile`
- `user_dashboard`
- `inventory_list`
- `item_detail`
- `borrow_request`
- `reservation_list`
- `my_borrowings`
- `lost_report`
- `admin_dashboard`
- `item_manage`
- `item_create`
- `item_edit`
- `borrow_requests`
- `user_manage`
- `reports`

The forgot password page currently posts to the current URL and the login link uses a placeholder anchor for password help. Add a backend password reset URL when that flow is defined.

## Connecting Real Data

1. Add `inventory_project_frontend/templates` to Django `TEMPLATES["DIRS"]` or move these templates into your Django app template directory.
2. Add `inventory_project_frontend/static` to `STATICFILES_DIRS` or move the static files into the project static directory.
3. Create Django views using the context names listed above.
4. Replace disabled placeholder buttons with forms or links after permissions and business rules are ready.
5. Use `{% include "components/status_badge.html" with status=item.status %}` anywhere a consistent status badge is needed.
6. For charts, inject safe JSON before `dashboard_charts.js`, for example:

```html
<script>
  window.dashboardChartData = {
    borrowedLabels: ["Jan", "Feb", "Mar"],
    borrowedByMonth: [4, 7, 3],
    adminMostBorrowed: {
      labels: ["ESP32", "Arduino"],
      values: [12, 9]
    }
  };
</script>
```

## Notes For The Team

- The scaffold uses custom CSS rather than a framework dependency, with Bootstrap/Tailwind-like component naming.
- Empty states are built into tables and inventory grids with `{% empty %}`.
- Forms use normal HTML names so Django forms can replace them gradually.
- Admin sidebar links are visible by default for frontend review. Hide them later based on role or permission checks.
