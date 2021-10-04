from django.contrib import admin
from .models import SalePoint, Supplier
# Register your models here.

admin.site.register(Supplier)
admin.site.register(SalePoint)