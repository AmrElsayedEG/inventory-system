from collections import namedtuple
from django.urls import path
from .views import (
    ListRepresentitivesInMyStoreView, CreateDeliveryView, GetDeleteDeliveryView, CreateSalePointInvoiceyView, 
    ListSalePointInvoiceView, ModifySalePointInvoiceView, ListOutDeliveryView,
)
app_name = 'delivery'

urlpatterns = [

    path('reps/', ListRepresentitivesInMyStoreView.as_view(), name='reps_in_my_store'),

    path('create/', CreateDeliveryView.as_view(), name='create_delivery'),

    path('modify/<int:pk>/', GetDeleteDeliveryView.as_view(), name='modify_delivery'),

    path('list/', ListOutDeliveryView.as_view(), name='list_delivery'),

    path('salepoint/create/', CreateSalePointInvoiceyView.as_view(), name='create_sale_point_delivery'),

    path('salepoint/list/', ListSalePointInvoiceView.as_view(), name='list_sale_point_delivery'),

    path('salepoint/modify/<int:pk>/', ModifySalePointInvoiceView.as_view(), name='modify_sale_point_delivery'),
]
