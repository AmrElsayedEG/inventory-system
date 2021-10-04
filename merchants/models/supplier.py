from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    category = models.ManyToManyField('products.Category')

    class Meta:
        db_table = 'supplier'
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'

    def __str__(self) -> str:
        return self.name