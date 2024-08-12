from django.urls import path
from .views import LocationHistoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"phone_locations", LocationHistoryViewSet, basename="phone_locations")

urlpatterns = router.urls