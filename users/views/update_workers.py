from rest_framework.generics import UpdateAPIView
from utils import IsManagerUser, IsAuthenticated
from users.models import User, Worker
from users.serializers import WorkersSerializer, UserSerializer
from rest_framework.response import Response


class UpdateUserView(UpdateAPIView):
   queryset = User
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated, IsManagerUser]

   def put(self, request, *args, **kwargs):

       self.partial_update(request, *args, **kwargs)

       return Response({
         "success": "Store Updated.",
         "success_ar" : "تم التحديث."
         })

class UpdateWorkerView(UpdateAPIView):
   queryset = Worker
   serializer_class = WorkersSerializer
   permission_classes = [IsAuthenticated, IsManagerUser]

   def get_object(self, *args, **kwargs):

       instance = User.objects.filter(pk=self.kwargs['pk'])

       if not instance.exists():
           raise ValueError('User not found')

       instance = instance.last()._user_worker

       if not instance.exists():
           raise ValueError('Worker not found')
       
       return instance.last()

   def put(self, request, *args, **kwargs):

       self.partial_update(request, *args, **kwargs)

       return Response({
         "success": "Store Updated.",
         "success_ar" : "تم التحديث."
         })