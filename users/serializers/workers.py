from rest_framework import serializers
from users.models import Worker
from .user import UserSerializer, BasicUserInfoSerializer
from store.serializers import ListUpdateStoreSerializer

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = UserSerializer(instance.user).data
        data['store'] = ListUpdateStoreSerializer(instance.store).data
        return data

class BasicWorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = BasicUserInfoSerializer(instance.user).data
        data['store'] = ListUpdateStoreSerializer(instance.store).data
        return data