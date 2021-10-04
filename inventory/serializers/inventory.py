from rest_framework import serializers
from django.core.exceptions import ValidationError
from inventory.models import Inventory
from store.serializers import ListUpdateStoreSerializer
from products.serializers import ProductSerializer

class StoreKeeperInventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ('id', 'store', 'product', 'boxs', 'box_items', 'expiry_date', 'arrival_date', 'items_left',)
        extra_kwargs = {'arrival_date' : {'read_only' : True}}

    def validate(self, attrs):
        attrs['items_left'] = int(attrs['boxs']) * int(attrs['box_items'])
        return attrs

    def to_representation(self, instance):

        result = super(StoreKeeperInventorySerializer, self).to_representation(instance)
        result['store'] = ListUpdateStoreSerializer(instance.store).data
        result['product'] = ProductSerializer(instance.product).data
        result['expiry_date'] = instance.expiry_date.strftime('%d-%m-%Y') if instance.expiry_date else None
        result['arrival_date'] = instance.arrival_date.strftime('%d-%m-%Y %H:%M:%S')

        return result

class InventorySerializer(serializers.ModelSerializer):

    total_price = serializers.FloatField()

    class Meta:
        model = Inventory
        fields = ('id', 'store', 'product', 'boxs', 'box_items', 'expiry_date', 'box_price', 'item_price', 'arrival_date', 'total_price', 'items_left',)
        extra_kwargs = {'total_price' : {'read_only' : True}}

    def get_total_price(self, instance):
        return instance.total_price()

    def to_representation(self, instance):

        result = super(InventorySerializer, self).to_representation(instance)
        result['store'] = ListUpdateStoreSerializer(instance.store).data
        result['product'] = ProductSerializer(instance.product).data
        result['expiry_date'] = instance.expiry_date.strftime('%d-%m-%Y') if instance.expiry_date else None
        result['arrival_date'] = instance.arrival_date.strftime('%d-%m-%Y %H:%M:%S')

        return result
