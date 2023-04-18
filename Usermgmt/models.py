from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.postgres.fields import ArrayField

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
    ("Anonymous", "Anonymous"),
)

class AccountManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("is_staff is set to False")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser is set to False")
        return self.create_user(email, password, **other_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    phone_no = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER, max_length=10)
    country = models.CharField(max_length=50)
    interests = ArrayField(models.CharField(max_length=20), default=list)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email