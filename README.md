# Capstone-project
App-Level URLs (restaurant.urls)
Menu Items List and Creation

URL: /restaurant/menu/
Method: GET to retrieve a list of menu items, POST to create a new menu item.
View: MenuItemsView
Single Menu Item Details, Update, and Delete

URL: /restaurant/menu/<int:pk>/
Method: GET to retrieve details of a single menu item, PUT to update it, and DELETE to delete it.
View: SingleMenuItemView
Custom Message Endpoint

URL: /restaurant/message/
Method: Typically GET (depends on how the msg view is defined).
View: msg (function-based view).
Project-Level URLs
Booking ViewSet (with DRF Router)

URL Base: /restaurant/booking/tables/
Automatically handles:
GET (list and detail views),
POST (create),
PUT/PATCH (update),
DELETE (delete).
ViewSet: BookingViewSet
Djoser Authentication URLs

Base URL for Djoser: /auth/
Includes endpoints for:
User registration,
User login (/auth/token/login/),
User logout (/auth/token/logout/).
Token Authentication Endpoint

URL: /api-token-auths/
Method: POST with username and password to obtain an authentication token.
View: obtain_auth_token (from rest_framework.authtoken.views).