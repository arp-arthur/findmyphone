from django.urls import path
from .views import PhoneViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"phones", PhoneViewSet, basename="phone")

urlpatterns = router.urls