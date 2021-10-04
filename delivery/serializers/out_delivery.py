from rest_framework import serializers
from delivery.models import OutDelivery
from delivery.serializers import OutProductSerializer
from django.core.exceptions import ValidationError

class OutDeliverySerializer(serializers.ModelSerializer):

    error_msg = {
        'wrong_delivery' : {
            'error' : 'These products already shipped',
            'error_ar' : 'هذه المنتجات تم شحنها',
        }
    }

    class Meta:
        model = OutDelivery
        fields = '__all__'

    def validate(self, attrs):
        
        products = [i.id for i in attrs['products']]

        if OutDelivery.objects.filter(store=attrs['store'], products__in=products).exists():
            for i in attrs['products']:
                i.delete()
            raise ValidationError(self.error_msg['wrong_delivery'])
        
        return attrs

    def to_representation(self, instance):
        result = super(OutDeliverySerializer, self).to_representation(instance)
        result['products'] = OutProductSerializer(instance.products, many=True).data
        return result