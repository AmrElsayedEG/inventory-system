from rest_framework.generics import CreateAPIView
from utils import IsManagerUser, IsAuthenticated
from merchants.models import SalePoint
from merchants.serializers import SalePointSerializer


class CreateSalePointView(CreateAPIView):
   queryset = SalePoint
   serializer_class = SalePointSerializer
   permission_classes = [IsAuthenticated]