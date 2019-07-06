from django.urls import path,include
from Account import views



urlpatterns = [
    path('register', views.register, name='register'),
    path('add_customer/',views.add_customer,name='add_customer'),
]