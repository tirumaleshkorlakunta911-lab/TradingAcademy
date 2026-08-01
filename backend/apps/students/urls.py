from django.urls import path

from .views import (
    StudentProfileView,
    StudentDashboardView,
)

urlpatterns = [

    path(
        "profile/",
        StudentProfileView.as_view(),
        name="student-profile",
    ),

    path(
        "dashboard/",
        StudentDashboardView.as_view(),
        name="student-dashboard",
    ),

]