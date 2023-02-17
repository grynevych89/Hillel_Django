from django.db import models


class Rate(models.Model):
    currency = models.CharField('Валюта', max_length=25)
    sell = models.DecimalField('Продаж', max_digits=6, decimal_places=2)
    buy = models.DecimalField('Покупка', max_digits=6, decimal_places=2)
    source = models.CharField('Банк', max_length=25)
    created = models.DateTimeField('Дата створення', auto_now_add=True)

    def __str__(self):
        return self.currency

    class Meta:
        verbose_name = "Курс валют"
        verbose_name_plural = "1. Курс валют"


class ContactUs(models.Model):
    subject = models.CharField('Тема', max_length=128)
    email_from = models.EmailField('email', blank=False)
    message = models.TextField('Текст звернення', max_length=2056, null=True, blank=True)

    def __str__(self):
        return self.email_from

    class Meta:
        verbose_name = "Звернення кліентів"
        verbose_name_plural = "2. Звернення кліентів"
