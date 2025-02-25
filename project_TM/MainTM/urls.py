from django.urls import path 
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'MainTM'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('automoveis/', views.buscar_automoveis, name='buscar_automoveis'),
    path('pecas/', views.buscar_pecas, name='buscar_pecas'),
    path('automoveis/<str:codigo_fipe>/', views.detalhe_automovel, name='detalhe_automovel'),
    path('pecas/<int:peca_id>/', views.detalhe_peca, name='detalhe_peca'),
    path('recomendacoes/', views.obter_recomendacoes_automoveis, name='recomendacoes_automoveis'),
    path('consultar-veiculo/', views.consultar_veiculo_fipe, name='consultar_veiculo_fipe'),
    

]