from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('verificar/',views.verificar,name='verificar'),
    path('votacao/',views.votacao,name='votacao'),


    
]