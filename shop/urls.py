from django.urls import include, path

from .views import UserListCreateView, UserDetailView, LogoutView, OrderCreateView

urlpatterns = [
    path("all-profiles", UserListCreateView.as_view(), name="all-profiles"),
    path("profile/<slug:pk>", UserDetailView.as_view(), name="profile"),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('order/', OrderCreateView.as_view(), name='order_create' )
]