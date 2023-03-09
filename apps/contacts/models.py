from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=128, default='')
    subject = models.CharField('Тема', max_length=128)
    email_from = models.EmailField('email', blank=False)
    message = models.TextField('Текст звернення', max_length=2056, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звернення кліентів"
        verbose_name_plural = "Звернення кліентів"


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=256)
    request_method = models.CharField(max_length=16)
    time = models.FloatField()
