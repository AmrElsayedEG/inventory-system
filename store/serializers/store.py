from rest_framework import serializers
from store.models import Store
from django.core.exceptions import ValidationError

class ListUpdateStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class CreateStoreSerializer(serializers.ModelSerializer):
    error_msg = {
        'dublicated' : {
            'error' : 'A store with this name is already existed.',
            'error_ar' : 'يوجد مخزن بهذا الأسم مسجل مسبقاً.',
        }
    }
    class Meta:
        model = Store
        fields = '__all__'

    def validate(self, attrs):
        if Store.objects.filter(name=attrs['name']).exists():
            raise ValidationError(self.error_msg['dublicated'])
        return attrs