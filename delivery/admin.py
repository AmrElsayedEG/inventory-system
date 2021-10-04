from django.contrib import admin
from .models import OutDelivery, OutProduct, SalePointDelivery, SalePointInvoice
# Register your models here.

admin.site.register(OutProduct)
admin.site.register(OutDelivery)
admin.site.register(SalePointDelivery)
admin.site.register(SalePointInvoice)