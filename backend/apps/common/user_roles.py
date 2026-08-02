from apps.students.models import Student
from apps.subscriptions.models import PremiumSubscription


def is_student(user):
    return Student.objects.filter(
        user=user,
        status="ACTIVE",
    ).exists()


def is_premium(user):
    return PremiumSubscription.objects.filter(
        user=user,
        status="ACTIVE",
    ).exists()


def get_user_roles(user):
    roles = ["ALL"]

    if is_student(user):
        roles.append("STUDENT")

    if is_premium(user):
        roles.append("PREMIUM")

    return roles