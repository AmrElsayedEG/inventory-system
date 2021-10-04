from rest_framework.generics import ListAPIView
from utils import IsAuthenticated, IsStockKeeperUser, IsManagerUser
from inventory.serializers import StoreKeeperInventorySerializer, InventorySerializer
from inventory.models import Inventory


class StoreKeeperListInventoryView(ListAPIView):
   queryset = Inventory
   serializer_class = StoreKeeperInventorySerializer
   permission_classes = [IsAuthenticated, IsStockKeeperUser]

   def get_queryset(self):
       worker = self.request.user._user_worker.last()
       if worker:
         return Inventory.objects.filter(box_price__isnull=False, item_price__isnull=False, store=worker.store).order_by('-arrival_date')
       return []


class ListInventoryView(ListAPIView):
   queryset = Inventory.objects.all()
   serializer_class = InventorySerializer
   permission_classes = [IsAuthenticated, IsManagerUser]