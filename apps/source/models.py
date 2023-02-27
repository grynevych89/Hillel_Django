from django.db import models


class Source(models.Model):
    name = models.CharField('Название', max_length=64)
    text = models.TextField('Описание')
    source_url = models.URLField('URL', max_length=255)
    price = models.PositiveIntegerField('Ціна', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Source"
        verbose_name_plural = "Source"
