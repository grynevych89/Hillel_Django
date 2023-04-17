from rest_framework.routers import DefaultRouter
from contacts.api.v1.views import ContactUsViewSet

app_name = 'api-contactus'

router = DefaultRouter()
router.register(r'', ContactUsViewSet, basename='contactsus')

urlpatterns = [

]

urlpatterns += router.urls
