import email
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for the user profile"""

    def create_user(self, name, email, password=None):
        """Create new user profile"""
        if not email:
            return ValueError("Youser must have an email address")

        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        "Creating the new super user with the given details"

        user = self.create_user(self, email, name, password)
        user.is_superuser == True
        user.is_staff == True
        user.save(self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the user in database"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)



    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = 'name'

    def get_full_name(self):
        """Retirve the full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrive the short name of the user"""
        return self.name

    def __str__(self):
        """Retrurn string representation of our model"""
        return self.email