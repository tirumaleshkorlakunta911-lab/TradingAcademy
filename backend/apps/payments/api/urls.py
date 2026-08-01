from django.urls import path

from .views import CreatePremiumOrderView

urlpatterns = [
    path(
        "premium/create-order/",
        CreatePremiumOrderView.as_view(),
        name="create-premium-order",
    ),
]