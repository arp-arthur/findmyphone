from django.db import models
from common.models import Base
from phones.models import Phone
from django.contrib.gis.db import models as gis_models

# Create your models here.
class LocationHistory(Base):
    phone = models.ForeignKey(Phone, related_name="history", on_delete=models.CASCADE)
    location = gis_models.PointField()
    battery = models.IntegerField()
    wifi = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Location History"
        verbose_name_plural = "Locations History"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.phone.phone_model}: {self.location} - {self.battery} - {self.wifi} - {self.dt_creation}"