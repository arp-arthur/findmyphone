from django.db import models

# Create your models here.
class Base(models.Model):
    dt_creation = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
