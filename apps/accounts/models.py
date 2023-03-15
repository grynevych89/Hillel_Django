import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    unique_id = models.UUIDField(default=uuid.uuid4, unique=True)
    username = models.CharField(unique=True, max_length=128)
    email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']
