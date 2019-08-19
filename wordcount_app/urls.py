from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage),
    path('egg/', views.egg, name='egg'),
    
]