from .models import Notification

from apps.students.models import Student
from apps.subscriptions.models import PremiumSubscription


class NotificationService:

    @staticmethod
    def create_notification(
        user,
        title,
        message,
        notification_type="GENERAL",
        announcement=None,
    ):

        return Notification.objects.create(
            user=user,
            title=title,
            message=message,
            notification_type=notification_type,
            announcement=announcement,
        )

    @staticmethod
    def send_to_students(
        title,
        message,
        announcement=None,
    ):

        students = Student.objects.filter(
            status="ACTIVE",
        )

        for student in students:

            NotificationService.create_notification(
                user=student.user,
                title=title,
                message=message,
                notification_type="CLASS",
                announcement=announcement,
            )

    @staticmethod
    def send_to_premium(
        title,
        message,
        announcement=None,
    ):

        subscriptions = PremiumSubscription.objects.filter(
            status="ACTIVE",
        )

        for subscription in subscriptions:

            NotificationService.create_notification(
                user=subscription.user,
                title=title,
                message=message,
                notification_type="TIPS",
                announcement=announcement,
            )