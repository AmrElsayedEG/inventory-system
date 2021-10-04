from rest_framework.generics import CreateAPIView
from utils import IsAuthenticated, ProductModifyUser
from products.serializers import ProductSerializer
from products.models import Product


class CreateProductView(CreateAPIView):
   queryset = Product
   serializer_class = ProductSerializer
   permission_classes = [IsAuthenticated, ProductModifyUser]