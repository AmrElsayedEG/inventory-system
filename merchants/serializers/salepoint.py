from rest_framework import serializers
from merchants.models import SalePoint
from django.core.exceptions import ValidationError

class SalePointSerializer(serializers.ModelSerializer):

    error_msg = {
        'dub_name' : {
            'error' : 'A sale point with that name already exists.',
            'error_ar' : 'توجد نقطة توزيع مسجل بهذا الأسم مسبقا.'
        }
    }

    class Meta:
        model = SalePoint
        fields = '__all__'

    def validate(self, attrs):
        if SalePoint.objects.filter(name__iexact=attrs['name'], address=attrs['address']).exists():
            raise ValidationError(self.error_msg['dub_name'])
        return attrs