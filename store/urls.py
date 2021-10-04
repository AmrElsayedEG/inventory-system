from django.urls import path
from store.views import CreateStoreView, ListStoresView, UpdateDeleteStoresView
app_name = 'store'

urlpatterns = [

    path('list/', ListStoresView.as_view(), name='list_stores'),
    path('create/', CreateStoreView.as_view(), name='create_store'),
    path('modify/<int:pk>/', UpdateDeleteStoresView.as_view(), name='modify_store'),
    
]
