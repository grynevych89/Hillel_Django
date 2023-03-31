from celery import shared_task
import requests
from currency.constants import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME
from currency.utils import to_2_places_decimal


@shared_task
def parse_privatbank():
    from currency.models import Rate, RateSource, RateCurrencyChoices

    source, _ = RateSource.objects.get_or_create(
        code_name=PRIVATBANK_CODE_NAME,
        defaults={
            'title': 'PrivatBank',
        }
    )

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate['ccy'] not in available_currency:
            continue

        buy = to_2_places_decimal(rate['buy'])
        sale = to_2_places_decimal(rate['sale'])
        currency = rate['ccy']

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source
        ).order_by('-created').first()

        if not last_rate or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source
            )


@shared_task
def parse_monobank():
    from currency.models import Rate, RateSource, RateCurrencyChoices

    source, _ = RateSource.objects.get_or_create(
        code_name=MONOBANK_CODE_NAME,
        defaults={
            'title': 'MonoBank',
        }
    )

    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    _USD = 840
    _EURO = 978

    available_currency = {
        _USD: RateCurrencyChoices.USD,
        _EURO: RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate['currencyCodeA'] not in available_currency:
            continue

        if rate['currencyCodeB'] == 980:
            buy = to_2_places_decimal(rate['rateBuy'])
            sale = to_2_places_decimal(rate['rateSell'])
            currency = rate['currencyCodeA']

            last_rate = Rate.objects.filter(
                currency=available_currency[currency],
                source=source
            ).order_by('-created').first()

            if not last_rate or last_rate.buy != buy or last_rate.sale != sale:
                Rate.objects.create(
                    buy=buy,
                    sale=sale,
                    currency=available_currency[currency],
                    source=source
                )
