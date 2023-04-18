from rest_framework.routers import DefaultRouter
from source.api.v1.views import SourceViewSet

app_name = 'api-source'

router = DefaultRouter()
router.register(r'', SourceViewSet, basename='sources')

urlpatterns = [

]

urlpatterns += router.urls
