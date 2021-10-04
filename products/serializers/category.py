from rest_framework import serializers
from products.models import Category
from django.core.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, attrs):
        if Category.objects.filter(name=attrs['name']).exists():
            raise ValidationError({
                'error' : 'This category already exists',
                'error_ar' : 'هذا التصنيف موجود بالفعل'
            })
        return attrs