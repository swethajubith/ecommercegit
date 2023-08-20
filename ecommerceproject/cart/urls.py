from django.urls import path
from.import views
app_name='cart'
urlpatterns = [
    path('add/<int:productid>/',views.addcart,name='addcart'),
    path('cart',views.cartdetail,name='cartdetail'),
    path('remove/<int:productid>/',views.cartremove,name='cartremove'),
    path('fullremove/<int:productid>/',views.fullremove,name='fullremove'),
]