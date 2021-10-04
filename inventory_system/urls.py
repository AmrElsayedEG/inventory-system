"""inventory_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),

    path('auth/', include('authentication.urls', namespace='aith')),

    path('users/', include('users.urls', namespace='users')),

    path('store/', include('store.urls', namespace='store')),

    path('products/', include('products.urls', namespace='products')),

    path('merchants/', include('merchants.urls', namespace='merchants')),

    path('inventory/', include('inventory.urls', namespace='inventory')),

    path('delivery/', include('delivery.urls', namespace='delivery')),
    
    path('bills/', include('bills.urls', namespace='bills')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
