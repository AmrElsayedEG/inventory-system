from rest_framework.generics import CreateAPIView
from utils import IsManagerUser, IsAuthenticated
from merchants.models import Supplier
from merchants.serializers import SupplierSerializer


class CreateSupplierView(CreateAPIView):
   queryset = Supplier
   serializer_class = SupplierSerializer
   permission_classes = [IsAuthenticated, IsManagerUser]