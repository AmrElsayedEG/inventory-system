from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from utils import IsManagerUser, IsAuthenticated
from merchants.models import Supplier
from merchants.serializers import SupplierSerializer, ModifySupplierSerializer
from rest_framework.response import Response


class ListSupplierView(ListAPIView):
   queryset = Supplier.objects.all()
   serializer_class = SupplierSerializer
   permission_classes = [IsAuthenticated]

class ModifySupplierView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier
    serializer_class = ModifySupplierSerializer
    permission_classes = [IsAuthenticated, IsManagerUser]

    def delete(self, request, *args, **kwargs):
        super(ModifySupplierView, self).delete(request, *args, **kwargs)
        return Response({
            'success' : 'Supplier deleted.',
            'success_ar' : 'تم حذف المورد.'
        })
