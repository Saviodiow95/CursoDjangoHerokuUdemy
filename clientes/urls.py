

from django.urls import path
from .views import *



urlpatterns = [
    path('listar/', listar, name='pessoa_listar'),
    path('nova/', nova, name='pessoa_nova'),
    path('atualizar/<int:id>', atualizar, name='pessoa_atuzalizar'),
    path('deletar/<int:id>', deletar, name='pessoa_deletar'),
]
