from rest_framework.generics import RetrieveUpdateDestroyAPIView
from utils import IsAuthenticated, ProductModifyUser
from products.serializers import ProductSerializer
from products.models import Product
from rest_framework.response import Response


class ModifyProductsView(RetrieveUpdateDestroyAPIView):
   queryset = Product
   serializer_class = ProductSerializer
   permission_classes = [IsAuthenticated, ProductModifyUser]

   def delete(self, request, *args, **kwargs):
        super(ModifyProductsView, self).delete(request, *args, **kwargs)
        return Response({
            'success' : 'Product deleted.',
            'success_ar' : 'تم حذف المنتج.'
        })