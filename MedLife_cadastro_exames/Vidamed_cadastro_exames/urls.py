from django.urls import path
from app_cad_exames import views

urlpatterns = [
    # rota, view, nome 
    path('',views.home,name= 'home'),
    path('ver_exames/', views.ver_exames, name='ver_exames'),
    path('cadastrar_exame/', views.cadastrar_exame, name='cadastrar_exame'),
    path('cadastrar_me/', views.cadastrar_me, name='cadastrar_me'),
]
