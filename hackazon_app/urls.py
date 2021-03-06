from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('cart-item/', views.cart_item ),
    path('search', views.search, name='search'),
    path('office', views.office, name='office'),
    path('kitchen', views.kitchen, name='kitchen'),
    path('garage', views.garage, name='garage'),
    path('livingroom', views.livingroom, name='livingroom'),
    path('patio', views.patio, name='patio'),
    path('products', views.products, name='products'),
]
