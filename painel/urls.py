from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel_overview, name='painel_overview'),
    path('imoveis/', views.lista_imoveis, name='lista_imoveis'),
    path('imoveis/<int:id>/', views.detalhes_imovel, name='detalhes_imovel'),
    path('equipe/', views.equipe_view, name='equipe_view'),
    path('relatorios/', views.relatorios_view, name='relatorios_view'),
    path('modo-simulacao/', views.modo_simulacao, name='modo_simulacao'),
    path('comparador/', views.comparador_view, name='comparador_view'),
]
