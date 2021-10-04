from users.models.user import national_id
from rest_framework import serializers
from users.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.db.models import Q

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CreateUserWorkerSerializer(serializers.ModelSerializer):
    error_msg = {
        'dub_user' : {
            'error' : 'A user with that username already exists',
            'error_ar' : 'يوجد مستخدم مسجل مسبقاً باسم المستخدم ذلك'
        },
        'wrong_store' : {
            'error' : 'Invalid store data',
            'error_ar' : 'خطأ في المتجر',
        }
    }

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'phone', 'gender', 'type', 'national_id',)
        extra_kwargs = {'username' : {'required' : True}}

    def validate(self, attrs):

        attrs['email'] = f'{attrs["username"]}_{attrs["phone"]}@inventory.com'
        
        if User.objects.filter(Q(username=attrs['username']) | Q(email=attrs['email'])).exists():
            raise ValidationError(self.error_msg['dub_user'])

        attrs['password'] = make_password(attrs['password'])

        return attrs

class BasicUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'gender', 'type', 'phone',)