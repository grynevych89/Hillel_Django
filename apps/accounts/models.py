import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static


def avatar_path(instance, filename):
    return f"avatars/{instance.username}/{filename}"


class User(AbstractUser):
    unique_id = models.UUIDField(default=uuid.uuid4, unique=True)
    username = models.CharField(unique=True, max_length=128)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=64,
        unique=True,
        null=True,
        blank=True,
    )
    avatar = models.FileField(
        default=None,
        null=True,
        blank=True,
        upload_to=avatar_path)

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('avatar-default.jpg')

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']
