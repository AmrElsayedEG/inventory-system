from django.urls import path
from .views import (
    CreateProductView, ListProductsView, ModifyProductsView, 
    CreateCategoryView, ListCetegoryView, ModifyCategoryView,
)

app_name = 'products'

urlpatterns = [

    path('create/', CreateProductView.as_view(), name='create_product'),

    path('list/', ListProductsView.as_view(), name='list_products'),

    path('modify/<int:pk>/', ModifyProductsView.as_view(), name='modify_product'),

    path('category/create/', CreateCategoryView.as_view(), name='create_category'),

    path('category/list/', ListCetegoryView.as_view(), name='list_category'),

    path('category/modify/<int:pk>/', ModifyCategoryView.as_view(), name='modify_category'),
    
]
