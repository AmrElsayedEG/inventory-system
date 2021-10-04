from django.db import models

class Product(models.Model):
    supplier = models.ForeignKey('merchants.supplier', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ForeignKey('products.category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self) -> str:
        return self.title