from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Announcement
from apps.notifications.services import NotificationService


@receiver(post_save, sender=Announcement)
def create_notifications(sender, instance, created, **kwargs):

    if not created:
        return

    if not instance.is_active:
        return

    if instance.target_audience == "STUDENT":

        NotificationService.send_to_students(
            title=instance.title,
            message=instance.message,
            announcement=instance,
        )

    elif instance.target_audience == "PREMIUM":

        NotificationService.send_to_premium(
            title=instance.title,
            message=instance.message,
            announcement=instance,
        )