from rest_framework.generics import RetrieveUpdateDestroyAPIView
from utils import IsManagerUser, IsAuthenticated
from store.models import Store
from store.serializers import ListUpdateStoreSerializer
from rest_framework.response import Response


class UpdateDeleteStoresView(RetrieveUpdateDestroyAPIView):
   queryset = Store
   serializer_class = ListUpdateStoreSerializer
   permission_classes = [IsAuthenticated, IsManagerUser]

   def delete(self, request, *args, **kwargs):
      super(UpdateDeleteStoresView, self).delete(request, *args, **kwargs)
      return Response({
         "success" : "Store Deleted.",
         "success_ar" : "تم حذف المتجر."
      })