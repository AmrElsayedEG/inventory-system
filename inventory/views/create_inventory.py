from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from utils import IsAuthenticated, IsStockKeeperUser
from inventory.serializers import StoreKeeperInventorySerializer
from inventory.models import Inventory


class CreateInventoryView(CreateAPIView):
   queryset = Inventory
   serializer_class = StoreKeeperInventorySerializer
   permission_classes = [IsAuthenticated, IsStockKeeperUser]

   def post(self, request, *args, **kwargs):
      data = self.request.data.copy()
      data['store'] = self.request.user._user_worker.last().store.id
      obj = self.serializer_class(data=data)
      obj.is_valid(raise_exception=True)
      obj.save()
      return Response(obj.data, status=201)