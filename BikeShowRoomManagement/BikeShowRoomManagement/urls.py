"""BikeShowRoomManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from bike import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.show_Home,name='home'),
    path('login/',views.login,name='login'),
    path('my_bike/', include('bike.urls')),
    path('my_booking/',include('booking.urls')),
    path('my_repair_bike/',include('repair_bike.urls')),
    path('my_insurance/',include('insurance.urls')),
    path('my_customer/',include('customer.urls')),
    path('my_accounts/',include('Account.urls')),
     path('my_payment/',include('payment.urls')),
    path('cart', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('', include('shop.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
