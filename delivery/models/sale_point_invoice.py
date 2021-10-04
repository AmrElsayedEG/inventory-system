from delivery.models import out_delivery
from django.db import models
from utils import PaymentMethodType
from utils import OutProductType

class SalePointInvoice(models.Model):
    out_delivery =  models.ForeignKey('delivery.outdelivery', on_delete=models.CASCADE)
    sale_point = models.ForeignKey('merchants.salepoint', on_delete=models.CASCADE)
    delivery_items = models.ManyToManyField('delivery.salepointdelivery')
    payment_method = models.CharField(choices=PaymentMethodType.choices, max_length=10)
    paid = models.BooleanField(default=False)
    delivery_date = models.DateTimeField(auto_now=True)

    def get_total_cost(self):
        total = 0
        for i in self.delivery_items.all():
            total += i.count * (i.product.inventory.box_price if i.product.type == OutProductType.BOXES else i.product.inventory.item_price)
        return total