from rest_framework import serializers
from delivery.models import OutProduct
from django.core.exceptions import ValidationError
from inventory.serializers import InventorySerializer

class OutProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutProduct
        fields = '__all__'

    def validate(self, attrs):

        if attrs['count'] > attrs['inventory'].items_left:
            raise ValidationError({
                'error' : f'{attrs["inventory"]} : The items are bigger than what is existe in the inventory',
                'error_ar' : f'{attrs["inventory"]} : القيمة المدخلة أكبر من المتواجد في المخزن',
            })

        attrs['count_left'] = attrs['count']

        return attrs

    def to_representation(self, instance):
        result = super(OutProductSerializer, self).to_representation(instance)
        result['inventory'] = InventorySerializer(instance.inventory).data
        return result