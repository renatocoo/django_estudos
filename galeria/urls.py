from django.urls import path
from galeria.views import index, imagem, novaAtividade

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('novaAtividade/', novaAtividade, name='novaAtividade')
]