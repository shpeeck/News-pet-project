from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=30, blank=False, null=True, unique=False)
    email = models.EmailField(_('Почта'), unique=True)
    email_verify = models.BooleanField(default=False)
    user_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

