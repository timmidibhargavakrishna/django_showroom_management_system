from django.urls import path
from payment import views
urlpatterns = [
   # path('admin/', admin.site.urls),
    #path('',views.index,name='index'),
    path('show_add_payment/',views.showPayment,name='show_add_payment'),
    path('add_payment/',views.addPayment,name='add_payment'),
    path('show_payment/',views.showEditPayment,name='show_payment'),
    path('edit_payment/',views.editPayment,name='edit_payment'),
    path('del_payment/',views.deletePayment,name='del_payment'),
    path('show_search_payment/',views.show_searchPayment,name='show_search_payment'),
    path('search_payment/',views.searchPayment,name='search_payment'),
]