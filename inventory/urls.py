from django.urls import path
from .views import (
    StoreKeeperListInventoryView, ListInventoryView, CreateInventoryView, StoreKeeperModifyInventoryView, ModifyInventoryView,
)

app_name = 'inventory'

urlpatterns = [

    path('storekeeper/list/', StoreKeeperListInventoryView.as_view(), name='store_keeper_list_inventory'),

    path('manager/list/', ListInventoryView.as_view(), name='manager_list_inventory'),

    path('storekeeper/create/', CreateInventoryView.as_view(), name='create_inventory'),

    path('storekeeper/modify/<int:pk>/', StoreKeeperModifyInventoryView.as_view(), name='store_keeper_modify_inventory'),

    path('manager/modify/<int:pk>/', ModifyInventoryView.as_view(), name='manager_modify_inventory'),
    
]
