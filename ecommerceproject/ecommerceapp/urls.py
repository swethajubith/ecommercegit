from django.urls import path
from.import views
app_name='ecommerceapp'
urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('slug/<slug:c_slug>/',views.allprodcat,name='products_by_category'),
    path('slug/<slug:c_slug>/<slug:product_slug>/',views.productdetail,name='prodcatdetail')
]