from django.urls import path

from .views import (
    FreeTipListView,
    PremiumTipListView,
)

urlpatterns = [
    path(
        "free/",
        FreeTipListView.as_view(),
        name="free-tips",
    ),

    path(
        "premium/",
        PremiumTipListView.as_view(),
        name="premium-tips",
    ),
]