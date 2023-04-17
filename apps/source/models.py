from django.db import models
from django.templatetags.static import static


def logo_path(instance, filename):
    return f"logos/{instance.name}/{filename}"


class Source(models.Model):
    name = models.CharField('Назва', max_length=64)
    text = models.TextField('Опис')
    source_url = models.URLField('URL', max_length=255)
    price = models.PositiveIntegerField('Ціна', default=0)
    logo = models.FileField(
        default=None,
        null=True,
        blank=True,
        upload_to=logo_path)

    @property
    def logo_url(self):
        if self.logo:
            return self.logo.url
        return static('default-logo.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Source"
        verbose_name_plural = "Source"
