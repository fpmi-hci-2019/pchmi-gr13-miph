from django.urls import path
from rest_framework.settings import api_settings
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:good_id>/', views.detail, name='detail'),

    path('search/', views.search, name='search'),
    path('catalog/', views.catalog, name='catalog'),

    path('cartView/', views.cartView, name='cartView'),
    path('userCabinet/', views.userCabinet, name='userCabinet'),

    path('cart/<int:good_id>', views.addToCart, name='addToCart'),
]