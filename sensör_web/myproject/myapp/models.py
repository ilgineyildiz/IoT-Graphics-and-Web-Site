# models.py
from django.db import models

class Device(models.Model):
    device_id = models.CharField(max_length=100, unique=True)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.device_id
