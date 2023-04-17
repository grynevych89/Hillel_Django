from rest_framework.throttling import AnonRateThrottle


class AnonContactUsThrottle(AnonRateThrottle):
    scope = 'contactus'
