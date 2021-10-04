from django.db import models

class SalePoint(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    coordinates = models.JSONField(blank=True, null=True)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'salepoint'
        verbose_name = 'salepoint'
        verbose_name_plural = 'salepoints'

    def __str__(self) -> str:
        return self.name