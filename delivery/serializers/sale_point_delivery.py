from rest_framework import serializers
from delivery.models import SalePointDelivery
from django.core.exceptions import ValidationError
from delivery.serializers import OutProductSerializer

class SalePointDeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = SalePointDelivery
        fields = '__all__'

    def to_representation(self, instance):
        result = super(SalePointDeliverySerializer, self).to_representation(instance)
        result['product'] = OutProductSerializer(instance.product).data
        return result

    def validate(self, attrs):
        if attrs['product'].delivered:
            raise ValidationError({
                    'error' : f'{attrs["product"].inventory.product.title} already delivered',
                    'error_ar' : f'{attrs["product"].inventory.product.title} تم تسليمة مسبقاً'
            })
        if attrs['count'] > attrs['product'].count_left:
            raise ValidationError({
                'error' : f'{attrs["product"].inventory.product.title} insufficient count',
                'error_ar' : f'{attrs["product"].inventory.product.title} الكمية أكبر من المتوفرة'
            })
        return attrs