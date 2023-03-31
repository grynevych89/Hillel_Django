from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    EUR = 1, 'Euro'
    USD = 2, 'Dollar'


class Rate(models.Model):
    created = models.DateTimeField('Дата створення', auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )
    buy = models.DecimalField('Покупка', max_digits=6, decimal_places=2)
    sale = models.DecimalField('Продаж', max_digits=6, decimal_places=2)
    source = models.ForeignKey('currency.RateSource', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'Currency: {self.get_currency_display()}'


class RateSource(models.Model):
    title = models.CharField('Банк', max_length=64)
    code_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.title
