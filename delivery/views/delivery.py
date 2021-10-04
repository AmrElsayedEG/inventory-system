from utils import OutDeliveryStatus
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.response import Response
from utils import IsAuthenticated, IsStockKeeperUser, UserTypeChoices
from delivery.models import OutProduct, OutDelivery
from delivery.serializers import OutProductSerializer, OutDeliverySerializer


class CreateDeliveryView(CreateAPIView):
    '''
        The data should be as follows
        {'products' : [OutProduct], 'representitive':user_id}
    '''
    queryset = OutProduct
    serializer_class = OutProductSerializer
    permission_classes = [IsAuthenticated, IsStockKeeperUser]

    def post(self, request, *args, **kwargs):
       current_store = self.request.user._user_worker.last()
       if not current_store:
           return Response({
               'error' : 'Invalid user store',
               'error_ar' : 'توجد مشكلة في المتجر الخاص بك',
           }, status=400)

       out_products = self.serializer_class(data=self.request.data['products'], many=True)
       out_products.is_valid(raise_exception=True)
       out_products = out_products.save()

       data = {
           'store' : current_store.store.id,
           'products' : [i.id for i in out_products],
           'representitive' : self.request.data['representitive'],
       }

       out_delivery = OutDeliverySerializer(data=data)
       out_delivery.is_valid(raise_exception=True)
       out_delivery.save()

       for i in out_products:
           i.inventory.items_left -= i.count
           i.inventory.save() 

       return Response({
           'sucecss' : 'Delivery created',
           'success_ar' : 'تم إنشاء الشحنة'
       })


class GetDeleteDeliveryView(RetrieveDestroyAPIView):
    queryset = OutDelivery
    serializer_class = OutDeliverySerializer
    permission_classes = [IsAuthenticated, IsStockKeeperUser]

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.status != OutDeliveryStatus.PENDING:
            return Response({
                'error' : 'This delivery in progress and can\'t be deleted',
                'error_ar' : 'هذه الشحنة قيد التوصيل ولا يمكن حذفها'
            }, status=400)
        return super(GetDeleteDeliveryView, self).delete(request)

class ListOutDeliveryView(ListAPIView):
    queryset = OutDelivery
    serializer_class = OutDeliverySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.type == UserTypeChoices.MANAGER:
            return OutDelivery.objects.all().order_by('-created_date')
        elif self.request.user.type == UserTypeChoices.STORE_KEEPER:
            return OutDelivery.objects.filter(store=self.request.user._user_worker.last().store.id).order_by('-created_date')
        elif self.request.user.type == UserTypeChoices.REPRESENTATIVE:
            return OutDelivery.objects.filter(representitive=self.request.user).order_by('-created_date')
        return []