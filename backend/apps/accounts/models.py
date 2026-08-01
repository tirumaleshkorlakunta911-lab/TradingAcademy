from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    USER_TYPES = (
        ("ADMIN", "Admin"),
        ("TRAINER", "Trainer"),
        ("STUDENT", "Student"),
    )

    username = None

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15, unique=True)

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default="STUDENT",
    )

    student_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    is_premium = models.BooleanField(default=False)

    accepted_risk = models.BooleanField(default=False)
    accepted_terms = models.BooleanField(default=False)
    accepted_privacy = models.BooleanField(default=False)

    accepted_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

    def __str__(self):
        return self.email