from rest_framework import serializers
from products.models import Product
from . import CategorySerializer
from merchants.serializers import SupplierSerializer
from django.core.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):

    error_msg = {
        'dub_product' : {
            'error' : 'This product already exists.',
            'error_ar' : 'هذا المنتج مسجل مسبقاً.'
        }
    }

    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, attrs):

        if Product.objects.filter(title=attrs['title'], supplier_id=attrs['supplier']).exists():
            raise ValidationError(self.error_msg['dub_product'])

        return attrs

    def to_representation(self, instance):

        result = super(ProductSerializer, self).to_representation(instance)
        result['supplier'] = SupplierSerializer(instance.supplier).data
        result['category'] = CategorySerializer(instance.category).data

        return result