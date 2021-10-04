from rest_framework import serializers
from merchants.models import Supplier
from products.serializers import CategorySerializer
from django.core.exceptions import ValidationError

class SupplierSerializer(serializers.ModelSerializer):

    error_msg = {
        'dub_name' : {
            'error' : 'A supplier with that name already exists.',
            'error_ar' : 'يوجد موزع مسجل بهذا الأسم مسبقا.'
        }
    }

    class Meta:
        model = Supplier
        fields = '__all__'

    def validate(self, attrs):
        if Supplier.objects.filter(name__iexact=attrs['name']).exists():
            raise ValidationError(self.error_msg['dub_name'])
        return attrs
        
    def to_representation(self, instance):

        result = super(SupplierSerializer, self).to_representation(instance)
        result['category'] = CategorySerializer(instance.category, many=True).data

        return result

class ModifySupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'