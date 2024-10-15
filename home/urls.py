from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('my_orders', views.my_orders, name='my_orders' )
]
