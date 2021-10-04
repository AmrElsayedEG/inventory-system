from rest_framework import serializers
from delivery.models import SalePointInvoice
from django.core.exceptions import ValidationError
from merchants.serializers import SalePointSerializer
from . import SalePointDeliverySerializer

class SalePointInvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalePointInvoice
        fields = '__all__'

    def to_representation(self, instance):
        result = super(SalePointInvoiceSerializer, self).to_representation(instance)
        result['sale_point'] = SalePointSerializer(instance.sale_point).data
        result['delivery_items'] = SalePointDeliverySerializer(instance.delivery_items, many=True).data
        result['payment_method'] = instance.get_payment_method_display()
        result['delivery_date'] = instance.delivery_date.strftime('%d-%m-%Y %H:%M:%S')
        result['total'] = instance.get_total_cost()
        return result
