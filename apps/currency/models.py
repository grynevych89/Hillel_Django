from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    EUR = 1, 'Euro'
    USD = 2, 'Dollar'


class Rate(models.Model):
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )
    sell = models.DecimalField('Продаж', max_digits=6, decimal_places=2)
    buy = models.DecimalField('Покупка', max_digits=6, decimal_places=2)
    source = models.CharField('Банк', max_length=25)
    created = models.DateTimeField('Дата створення', auto_now_add=True)

    def __str__(self):
        return f'Currency: {self.get_currency_display()}'
