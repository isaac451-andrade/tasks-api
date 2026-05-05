from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from .services import *

class TaskListView(ListAPIView):
    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Task.objects.filter(usuario=user)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def task_create_view(request: Request):
    task_kwargs = getTaskKwargs(request)

    if task_kwargs.get("titulo") is None:
        return Response({
            "erro": "O titulo da tarefa é obrigatório."
        }, status=403)
    
    tarefa = Task.objects.create(**task_kwargs)

    return Response({
        "data": f"Tarefa com id {tarefa.pk} criada com sucesso."
    }, status=201)


@api_view(["PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def task_update_view(request: Request, id: int):
    idLimpo = getIdLimpo(id)

    if idLimpo is None:
        return Response({
            "erro": f"Id {id} inválido.",
        }, status=403)
    
    update_kwargs = getValidUpdateKwargsForTask(request)

    if not update_kwargs:
        return Response({
            "erro": "Não foi fornecido nenhum campo válido para atualização. Mande algum desses campos: 'titulo', 'descricao', 'observacao', 'status' ",
        }, status=403)


    task_to_be_updated = Task.objects.filter(pk=idLimpo)

    if not task_to_be_updated.exists():
         return Response({
            "erro": f"Tarefa com id {idLimpo} não encontrado.",
        }, status=403)

    keys_for_save = list(update_kwargs.keys())

    task_to_be_updated = task_to_be_updated.first()

    task_to_be_updated.save(**update_kwargs, update_fields=keys_for_save)

    return Response({
        "data": "Tarefa atualizada com sucesso."
    }, 204)