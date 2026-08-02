from django.urls import path

from .views import (
    ResourceCategoryView,
    ResourceDetailView,
    ResourceListView,
)

urlpatterns = [

    path(
        "",
        ResourceListView.as_view(),
        name="resource-list",
    ),

    path(
        "<int:pk>/",
        ResourceDetailView.as_view(),
        name="resource-detail",
    ),

    path(
        "category/<str:category>/",
        ResourceCategoryView.as_view(),
        name="resource-category",
    ),
]