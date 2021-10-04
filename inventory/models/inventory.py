from django.db import models

class Inventory(models.Model):
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE)
    product = models.ForeignKey('products.product', on_delete=models.CASCADE)
    boxs = models.PositiveBigIntegerField()
    box_items = models.PositiveBigIntegerField()
    box_price = models.PositiveIntegerField(blank=True, null=True)
    item_price = models.PositiveIntegerField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    arrival_date = models.DateTimeField(auto_now_add=True)
    items_left = models.PositiveBigIntegerField(default=0)

    class Meta:
        db_table = 'inventory'
        verbose_name = 'inventory'
        verbose_name_plural = 'inventories'

    def __str__(self) -> str:
        return f'[Store :{self.store.name} - {self.product.title}] {self.arrival_date.strftime("%d-%m-%Y %H:%M:%S")}'

    def total_price(self):
        if self.item_price and self.box_items and self.box_items:
            return self.item_price * (self.box_items * self.boxs)
        return None