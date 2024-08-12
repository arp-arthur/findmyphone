from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin
from .models import LocationHistory
from phones.models import Phone
from .serializers import LocationHistorySerializer

# Create your views here.
class LocationHistoryViewSet(GenericViewSet, ListModelMixin, UpdateModelMixin, CreateModelMixin):
    queryset = LocationHistory.objects.all()
    serializer_class = LocationHistorySerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return LocationHistory.objects.all()
        
        return LocationHistory.objects.filter(phone__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)