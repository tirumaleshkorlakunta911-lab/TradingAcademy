from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/accounts/",
        include("apps.accounts.api.urls"),
    ),

    path(
        "api/subscriptions/",
        include("apps.subscriptions.api.urls"),
    ),

    path(
        "api/payments/",
        include("apps.payments.api.urls"),
    ),

    path(
        "api/tips/",
        include("apps.tips.api.urls"),
    ),

    path(
        "api/students/",
        include("apps.students.urls"),
    ),

    path(
        "api/classes/",
        include("apps.classes.urls"),
    ),

    path(
        "api/resources/",
        include("apps.resources.urls"),
    ),

    path(
        "api/attendance/",
        include("apps.attendance.urls"),
    ),

    path(
        "api/recordings/",
        include("apps.recordings.urls"),
    ),

    path(
        "api/announcements/",
        include("apps.announcements.urls"),
    ),

    path(
        "api/notifications/",
        include("apps.notifications.urls"),
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )