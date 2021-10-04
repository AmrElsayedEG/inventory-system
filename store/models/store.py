from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    coordinates = models.JSONField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name