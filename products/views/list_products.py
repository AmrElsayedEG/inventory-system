from rest_framework.generics import ListAPIView
from utils import IsAuthenticated
from products.serializers import ProductSerializer
from products.models import Product


class ListProductsView(ListAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   permission_classes = [IsAuthenticated]