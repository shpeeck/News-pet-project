from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, blank=False, null=True, unique=False)
    # first_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(_('Почта'), unique=True)
    email_verify = models.BooleanField(default=False)
    user_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

