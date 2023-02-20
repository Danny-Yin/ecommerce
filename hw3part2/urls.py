"""hw3part2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='Login'),
    path('Homepage', views.homepage_view, name='Homepage'),
    path('add_product/<int:product_id>', views.add_product, name='add_product'),
    path('myShoppingCart/', views.peronalshopping_cart, name='myShoppingCart'),
    path('add_number/<int:item_id>', views.add_number, name='add_number'),
    path('reduce_number/<int:item_id>', views.reduce_number, name='reduce_number'),
    path('no_number/<int:item_id>', views.no_number, name='no_number'),
]
