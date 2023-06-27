from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
<<<<<<< HEAD
    path('verificar/',views.verificar,name='verificar'),
=======
    path('verificar/',views.verificacao,name='verificar_senha'),
>>>>>>> 472e17593db4b5c461118f0c589efc0fe0489f69

    
]