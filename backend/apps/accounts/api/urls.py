from django.urls import path
from .profile_views import UserProfileView

from .auth_views import LoginView
from .views import UserRegistrationView

urlpatterns = [
    path(
        "register/",
        UserRegistrationView.as_view(),
        name="register",
    ),

    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),

    path(
        "profile/",
        UserProfileView.as_view(),
        name="profile",
    ),
]