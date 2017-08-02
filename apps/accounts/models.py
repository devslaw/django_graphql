from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            is_active=is_active,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    Types = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
        ('client', 'Client'),
    )
    user_type = models.CharField(
        max_length=20,
        choices=Types,
        default='client'
    )

    username = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    auth_key = models.CharField(blank=True, max_length=255)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=0)
    verification_code = models.CharField(blank=True, max_length=500)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

