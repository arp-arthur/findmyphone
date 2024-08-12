from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin
from .models import Phone
from .serializers import PhoneSerializer

# Create your views here.
class PhoneViewSet(GenericViewSet, ListModelMixin, UpdateModelMixin, CreateModelMixin):
    serializer_class = PhoneSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Phone.objects.all()
        
        return Phone.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)