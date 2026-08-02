from django.urls import path

from .views import (
    RecordingListView,
    RecordingDetailView,
    RecordingByClassView,
)

urlpatterns = [

    path(
        "",
        RecordingListView.as_view(),
        name="recording-list",
    ),

    path(
        "<int:pk>/",
        RecordingDetailView.as_view(),
        name="recording-detail",
    ),

    path(
        "class/<int:class_id>/",
        RecordingByClassView.as_view(),
        name="recording-by-class",
    ),

]