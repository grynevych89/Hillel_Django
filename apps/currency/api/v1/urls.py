from rest_framework.routers import DefaultRouter
from currency.api.v1.views import RateViewSet

app_name = 'api-currency'

router = DefaultRouter()
router.register(r'', RateViewSet, basename='rates')

urlpatterns = [

]

urlpatterns += router.urls
