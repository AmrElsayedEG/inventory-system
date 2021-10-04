from utils.choices import UserTypeChoices
from delivery.models.sale_point_invoice import SalePointInvoice
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from utils import IsAuthenticated, IsRepresentitiveUser
from delivery.models import SalePointDelivery
from delivery.serializers import SalePointDeliverySerializer, SalePointInvoiceSerializer, out_delivery


class CreateSalePointInvoiceyView(CreateAPIView):
    queryset = SalePointDelivery
    serializer_class = SalePointDeliverySerializer
    permission_classes = [IsAuthenticated, IsRepresentitiveUser]

    def post(self, request):
        if 'delivery_items' in self.request.data and 'sale_point' in self.request.data:
            delivery_items = self.serializer_class(data=self.request.data['delivery_items'], many=True)
            delivery_items.is_valid(raise_exception=True)
            delivery_items = delivery_items.save()

            data = self.request.data.copy()

            data['delivery_items'] = [i.id for i in delivery_items]

            invoice = SalePointInvoiceSerializer(data=data)
            if not invoice.is_valid():
                for i in delivery_items:
                    i.delete()
                    return Response(invoice.errors, status=400)
            invoice.save()

            for i in delivery_items:
                i.product.count_left -= i.count
                if i.product.count_left <= 0:
                    i.product.delivered = True
                i.product.save()

            return Response(invoice.data)

        return Response({
            'error' : 'Invalid data',
            'error_ar' : 'خطأ في البيانات'
        }, status=400)

class ListSalePointInvoiceView(ListAPIView):
    queryset = SalePointInvoice
    serializer_class = SalePointInvoiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.type == UserTypeChoices.REPRESENTATIVE:
            return SalePointInvoice.objects.filter(out_delivery__representitive=self.request.user.id).order_by('-delivery_date')
        elif self.request.user.type == UserTypeChoices.STORE_KEEPER:
            return SalePointInvoice.objects.filter(out_delivery__store=self.request.user._user_worker.last().store.id).order_by('-delivery_date')
        elif self.request.user.type == UserTypeChoices.MANAGER:
            return SalePointInvoice.objects.all().order_by('-delivery_date')
        return []

class ModifySalePointInvoiceView(RetrieveUpdateAPIView):
    queryset = SalePointInvoice
    serializer_class = SalePointInvoiceSerializer
    permission_classes = [IsAuthenticated]