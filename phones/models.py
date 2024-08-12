from django.db import models
from common.models import Base
from django.contrib.auth.models import User
# Create your models here.

class Phone(Base):
    user = models.ForeignKey(User, related_name="phones", on_delete=models.CASCADE)
    phone_model = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.phone_model