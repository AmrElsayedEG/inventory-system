from django.urls import path
from .views import ListWorkersView, CreateWorkerView, UpdateUserView, UpdateWorkerView

app_name = 'users'

urlpatterns = [

    path('workers/list/', ListWorkersView.as_view(), name='list_workers'),
    
    path('workers/create/', CreateWorkerView.as_view(), name='create_worker'),

    path('workers/update/user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),

    path('workers/update/worker/<int:pk>/', UpdateWorkerView.as_view(), name='update_worker'),
    
]
