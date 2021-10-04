from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from utils import IsManagerUser, IsAuthenticated
from users.models import User
from users.serializers import CreateUserWorkerSerializer, WorkersSerializer, workers

class CreateWorkerView(CreateAPIView):
   queryset = User
   serializer_class = CreateUserWorkerSerializer
   permission_classes = [IsAuthenticated, IsManagerUser]

   def create(self, request):
      user = CreateUserWorkerSerializer(data=self.request.data)
      user.is_valid(raise_exception=True)
      user = user.save()
      self.request.data['user'] = user.id
      worker = WorkersSerializer(data=self.request.data)
      if not worker.is_valid():
         user.delete()
         return Response(worker.errors, status=400)
      worker.save(user=user)
      return Response(worker.data)