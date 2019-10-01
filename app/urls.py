from django.urls import path
from .views.tarefa_views import *
from .views.usuario_views import *
urlpatterns = [
    path('listar_tarefas/', listar_tarefas, name='listar_tarefas'),
    path('', listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefa/', cadastrar_tarefa, name='cadastrar_tarefa'),
    path('editar_tarefa/<int:id>', editar_tarefa, name='editar_tarefa'),
    path('remover_tarefa/<int:id>', remover_tarefa, name='remover_tarefa'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('login/', logar_user, name='login'),
    path('logout/', deslogar_usuario, name='logout'),
]
