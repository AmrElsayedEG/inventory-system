from rest_framework.generics import CreateAPIView
from utils import IsManagerUser, IsAuthenticated
from store.models import Store
from store.serializers import CreateStoreSerializer


class CreateStoreView(CreateAPIView):
   queryset = Store.objects.all()
   serializer_class = CreateStoreSerializer
   permission_classes = [IsAuthenticated, IsManagerUser]