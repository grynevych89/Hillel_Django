from rest_framework.throttling import AnonRateThrottle


class AnonSourceThrottle(AnonRateThrottle):
    scope = 'source'
