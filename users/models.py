from django.db import models
from django.contrib.auth.models import User
from common.models import Base


# Create your models here.
class UserProfile(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    name=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.name if self.name else self.user.username