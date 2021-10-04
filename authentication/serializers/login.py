from rest_framework import serializers
from users.models import User

class LoginSerializer(serializers.ModelSerializer):

    error_msg = {
        "login" : {
            "error" : "Invalid Username or Password",
            "error_ar" : "خطأ في أسم المستخدم أو كلمة السر"
        },
        "not_active" : {
            "error" : "This account is not activated, Please contact the manager.",
            "error_ar" : "هذا الحساب غير مفعل، برجاء التواصل مع المدير."
        }
    }

    username = serializers.CharField(help_text="Enter Username here")
    password = serializers.CharField(help_text="Enter password here")

    class Meta:
        model = User
        fields = ('username', 'password',)

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).last()

        if not user:
            raise serializers.ValidationError(self.error_msg['login'])

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError(self.error_msg['login'])

        if not user.is_active:
            raise serializers.ValidationError(self.error_msg['not_active'])

        attrs['user'] = user

        return attrs