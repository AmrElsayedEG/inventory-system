from django.urls import path
from authentication.views import LoginView

app_name = 'users'

urlpatterns = [

    path('login/', LoginView.as_view(), name='login')
    
]
