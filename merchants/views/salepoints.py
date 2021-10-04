from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from utils import IsManagerUser, IsAuthenticated
from merchants.models import SalePoint
from merchants.serializers import SalePointSerializer
from rest_framework.response import Response


class ListSalePointsView(ListAPIView):
   queryset = SalePoint.objects.all()
   serializer_class = SalePointSerializer
   permission_classes = [IsAuthenticated]

class ModifySalePointView(RetrieveUpdateDestroyAPIView):
    queryset = SalePoint
    serializer_class = SalePointSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        super(ModifySalePointView, self).delete(request, *args, **kwargs)
        return Response({
            'success' : 'Salepoint deleted.',
            'success_ar' : 'تم حذف نقطة التوزيع.'
        })
