from rest_framework.request import Request
from django.utils.dateparse import parse_datetime

def getIdLimpo(id):
    try:
        idLimpo = int(str(id).strip().replace(".", ""))
    except Exception:
        idLimpo = None
    
    return idLimpo

def checkData(data_str):
    resultado = parse_datetime(data_str)
    
    return resultado is not None


def getStrLimpo(value:str | None):

    return str(value).strip() if value is not None else None


def getTaskKwargs(request: Request):

    status = getStrLimpo(request.data.get("status"))

    if status is None:
        status = "pendente"
    
    task_kwargs = {
        "titulo": getStrLimpo(request.data.get("titulo")),
        "descricao": getStrLimpo(request.data.get("descricao")),
        "observacao": getStrLimpo(request.data.get("observacao")),
        "usuario": request.user,
        "status": status,
        "data_conclusao": getStrLimpo(request.data.get("data_conclusao"))
    }

    return task_kwargs

def getValidUpdateKwargsForTask(request: Request):
    task_kwargs = getTaskKwargs(request)
    print(task_kwargs, "AAAA")
    
    update_kwargs = {k: v for k, v in task_kwargs.items() if v is not None}

    return update_kwargs
    
    