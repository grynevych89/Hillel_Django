from unittest.mock import MagicMock
from currency.tasks import parse_privatbank, parse_monobank
from currency.models import Rate


def test_privatbank_parser(mocker):
    initial_count = Rate.objects.count()
    privat_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "45.15050", "sale": "45.84100"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "30.56860", "sale": "30.45318"}
    ]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: privat_data,
        )
    )

    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2

    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2

    assert request_get_mock.call_count == 2


def test_monobank_parser(mocker):
    initial_count = Rate.objects.count()
    monobank_data = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1609204800, "rateBuy": 30.299, "rateSell": 30.599},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1609204800, "rateBuy": 45.299, "rateSell": 45.599},
    ]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: monobank_data,
        )
    )

    parse_monobank()
    assert Rate.objects.count() == initial_count + 2

    parse_monobank()
    assert Rate.objects.count() == initial_count + 2

    assert request_get_mock.call_count == 2
