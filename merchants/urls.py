from django.urls import path
from .views import (
    CreateSupplierView, ListSupplierView, ModifySupplierView, CreateSalePointView, ListSalePointsView, 
    ModifySalePointView,
)

app_name = 'merchants'

urlpatterns = [

    path('supplier/create/', CreateSupplierView.as_view(), name='create_supplier'),

    path('supplier/list/', ListSupplierView.as_view(), name='list_supplier'),

    path('supplier/modify/<int:pk>/', ModifySupplierView.as_view(), name='modify_supplier'),

    path('salepoint/create/', CreateSalePointView.as_view(), name='create_salepoint'),

    path('salepoint/list/', ListSalePointsView.as_view(), name='list_salepoint'),

    path('salepoint/modify/<int:pk>/', ModifySalePointView.as_view(), name='modify_salepoint'),
    
]
