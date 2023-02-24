from django.db import models


class ContactUs(models.Model):
    subject = models.CharField('Тема', max_length=128)
    email_from = models.EmailField('email', blank=False)
    message = models.TextField('Текст звернення', max_length=2056, null=True, blank=True)

    def __str__(self):
        return self.email_from

    class Meta:
        verbose_name = "Звернення кліентів"
        verbose_name_plural = "Звернення кліентів"
