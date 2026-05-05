from django.db import models
from django.conf import settings

class Task(models.Model):
    STATUS_CHOICES = [
        ("pendente", "PENDENTE"),
        ("em_andamento", "EM ANDAMENTO"),
        ("aguardando_dependencia", "AGUARDANDO DEPENDÊNCIA"),
        ("concluido", "CONCLUIDO"),
    ]
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    data_criacao = models.DateTimeField(auto_now_add=True, editable=False)
    data_conclusao = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="pendente")
