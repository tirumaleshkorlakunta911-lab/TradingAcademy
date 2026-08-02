from django.urls import path

from .views import (
    UpcomingClassesView,
    LiveClassDetailView,
    JoinClassView,
)

urlpatterns = [

    path(
        "upcoming/",
        UpcomingClassesView.as_view(),
        name="upcoming-classes",
    ),

    path(
        "<int:pk>/",
        LiveClassDetailView.as_view(),
        name="class-detail",
    ),

    path(
        "<int:pk>/join/",
        JoinClassView.as_view(),
        name="join-class",
    ),


]