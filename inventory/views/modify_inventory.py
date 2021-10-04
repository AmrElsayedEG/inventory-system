from rest_framework.generics import RetrieveUpdateDestroyAPIView
from utils import IsAuthenticated, IsStockKeeperUser, IsManagerUser
from inventory.serializers import StoreKeeperInventorySerializer, InventorySerializer
from inventory.models import Inventory
from rest_framework.response import Response



class StoreKeeperModifyInventoryView(RetrieveUpdateDestroyAPIView):
   queryset = Inventory
   serializer_class = StoreKeeperInventorySerializer
   permission_classes = [IsAuthenticated, IsStockKeeperUser]

   def delete(self, request, *args, **kwargs):
        super(StoreKeeperModifyInventoryView, self).delete(request, *args, **kwargs)
        return Response({
            'success' : 'Inventory item deleted.',
            'success_ar' : 'تم حذف الشحنة.'
        })

class ModifyInventoryView(RetrieveUpdateDestroyAPIView):
   queryset = Inventory
   serializer_class = InventorySerializer
   permission_classes = [IsAuthenticated, IsManagerUser]

   def delete(self, request, *args, **kwargs):
        super(ModifyInventoryView, self).delete(request, *args, **kwargs)
        return Response({
            'success' : 'Inventory item deleted.',
            'success_ar' : 'تم حذف الشحنة.'
        })