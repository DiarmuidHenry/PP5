from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('my_orders/<str:order_number>/', views.order_details, name='order_details'),
]
