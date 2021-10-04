from django.db import models
from utils import OutProductType
from inventory.models import Inventory

class OutProduct(models.Model):
    inventory = models.ForeignKey('inventory.inventory', on_delete=models.CASCADE)
    type = models.CharField(choices=OutProductType.choices, max_length=20)
    count = models.PositiveIntegerField()
    count_left = models.PositiveBigIntegerField(default=0)
    delivered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.inventory.product.title

    @property
    def get_total(self):
        if type == OutProductType.BOXES:
            return float(self.count * self.inventory.box_price)
        if type == OutProductType.ITEMS:
            return float(self.count * self.inventory.item_price)
        return None