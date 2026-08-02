from django.urls import path

from .views import MyAttendanceView

urlpatterns = [

    path(
        "me/",
        MyAttendanceView.as_view(),
        name="my-attendance",
    ),

]