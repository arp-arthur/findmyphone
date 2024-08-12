from django.urls import path
from .views import CreateUserAPIView, LoginUserAPIView, LogoutUserAPIView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("auth/login/", LoginUserAPIView.as_view(), name="auth_user_login"),
    path("auth/register/", CreateUserAPIView.as_view(), name="auth_user_create"),
    path("auth/logout/", LogoutUserAPIView.as_view(), name="auth_user_logout"),
]

urlpatterns += router.urls
