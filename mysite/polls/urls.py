from django.urls import path
from rest_framework.settings import api_settings
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:good_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:good_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:good_id>/vote/', views.vote, name='vote'),

    path('search/', views.search, name='search'),

    # path('search/<str:search_name>/searchResults', views.searchResults, name='searchResults'),

    path('catalog/', views.catalog, name='catalog'),

    path('cartView/', views.cartView, name='cartView'),
    path('userCabinet/', views.userCabinet, name='userCabinet'),

    path('cart/<int:good_id>', views.addToCart, name='addToCart'),
]