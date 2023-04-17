from rest_framework.throttling import AnonRateThrottle


class AnonCurrencyThrottle(AnonRateThrottle):
    scope = 'currency'
