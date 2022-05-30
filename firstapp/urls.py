from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('regi', views.regi, name='regi'),
    path('login', views.login, name='login'),
    path('userregister',views.userregister, name='userregister'),
    path('userlogin',views.userlogin, name='userlogin'),
    path('changepass',views.changepass, name='changepass'),
    path('changepasswordauth',views.changepasswordauth, name='changepasswordauth'),
    path('logout',views.logout, name='logout'),
    path('cart',views.cart, name='cart'),
    path('userpro',views.userpro, name='userpro'),
    path('editpro',views.editpro, name='editpro'),
    path('editauth',views.editauth, name='editauth'),
    path('addtocart',views.add_to_cart, name='cart'),
    path('product',views.product, name='product'),
]
