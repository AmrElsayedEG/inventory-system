from rest_framework.generics import ListAPIView
from utils import IsManagerUser, IsAuthenticated
from users.models import Worker
from users.serializers import WorkersSerializer


class ListWorkersView(ListAPIView):
   queryset = Worker.objects.all()
   serializer_class = WorkersSerializer
   permission_classes = [IsAuthenticated, IsManagerUser]