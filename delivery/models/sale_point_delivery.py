from django.db import models

class SalePointDelivery(models.Model):
    product = models.ForeignKey('delivery.outproduct', on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    