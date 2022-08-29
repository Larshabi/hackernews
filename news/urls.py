from django.urls import path
from .views import *

urlpatterns = [
   path('search/', search, name='search'),
   path('filter/<str:type>/', filter, name='filter'),
   path('filters/<str:type>/', Filter.as_view(), name='filters'),
   path('', ItemList.as_view(), name='home'),
   path('<int:pk>/', ItemDetail.as_view(), name='detail'),
]