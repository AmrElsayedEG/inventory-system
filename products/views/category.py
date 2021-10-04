from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from utils import IsAuthenticated, ProductModifyUser
from products.serializers import CategorySerializer
from products.models import Category
from rest_framework.response import Response


class CreateCategoryView(CreateAPIView):
   queryset = Category
   serializer_class = CategorySerializer
   permission_classes = [IsAuthenticated, ProductModifyUser]

class ListCetegoryView(ListAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   permission_classes = [IsAuthenticated, ProductModifyUser]

class ModifyCategoryView(RetrieveUpdateDestroyAPIView):
   queryset = Category
   serializer_class = CategorySerializer
   permission_classes = [IsAuthenticated, ProductModifyUser]

   def delete(self, request, *args, **kwargs):
        super(ModifyCategoryView, self).delete(request, *args, **kwargs)
        return Response({
            'success' : 'Category deleted.',
            'success_ar' : 'تم حذف التصنيف.'
        })