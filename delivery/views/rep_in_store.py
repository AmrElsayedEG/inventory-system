from rest_framework.generics import ListAPIView
from utils import IsAuthenticated, IsStockKeeperUser
from users.serializers import BasicWorkersSerializer
from users.models import Worker
from utils import UserTypeChoices


class ListRepresentitivesInMyStoreView(ListAPIView):
   queryset = Worker
   serializer_class = BasicWorkersSerializer
   permission_classes = [IsAuthenticated, IsStockKeeperUser]

   def get_queryset(self):
       try:
           store = self.request.user._user_worker.last().store
           return Worker.objects.filter(user__type=UserTypeChoices.REPRESENTATIVE, store=store)
       except:
            return []