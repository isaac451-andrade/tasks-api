from rest_framework.request import Request

def getIdLimpo(id):
    try:
        idLimpo = int(str(id).strip().replace(".", ""))
    except Exception:
        idLimpo = None
    
    return idLimpo



def getStrLimpo(value:str | None):

    return str(value).strip() if value is not None else None


def getTaskKwargs(request: Request):
    task_kwargs = {
        "titulo": getStrLimpo(request.data.get("titulo")),
        "descricao": getStrLimpo(request.data.get("descricao")),
        "observacao": getStrLimpo(request.data.get("observacao")),
        "usuario": request.user,
    }

    return task_kwargs

def getValidUpdateKwargsForTask(request: Request):
    task_kwargs = getTaskKwargs(request)

    update_kwargs = dict(filter(lambda value: value is not None, task_kwargs.values()))

    return update_kwargs
    
    