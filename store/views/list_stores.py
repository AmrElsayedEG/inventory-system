from rest_framework.generics import ListAPIView
from utils import IsAuthenticated
from store.models import Store
from store.serializers import ListUpdateStoreSerializer


class ListStoresView(ListAPIView):
   queryset = Store.objects.all()
   serializer_class = ListUpdateStoreSerializer
   permission_classes = [IsAuthenticated]