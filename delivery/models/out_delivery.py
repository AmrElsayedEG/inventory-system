from django.db import models
from utils import OutDeliveryStatus

class OutDelivery(models.Model):
    store = models.ForeignKey('store.store', on_delete=models.CASCADE)
    representitive = models.ForeignKey('users.user', on_delete=models.CASCADE)
    products = models.ManyToManyField('delivery.OutProduct')
    status = models.CharField(choices=OutDeliveryStatus.choices, default=OutDeliveryStatus.PENDING, max_length=20)
    created_date = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        total = float(0)
        for i in self.products:
            total += i.get_total()
        return total
