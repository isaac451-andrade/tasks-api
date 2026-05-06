import requests

def gerar_tokens_acesso(username: str, password: str):
    data = {
        "username": username.strip(),
        "password": password.strip()
    }

    response = requests.post("http://127.0.0.1:8000/api/v1/token/", data=data)

    dados = response.json()

    return dados


access = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4MDMwODkwLCJpYXQiOjE3NzgwMjcyOTAsImp0aSI6IjNiMjViNGJmM2VmYjRjY2I5ZTU3NDdkYWMxM2I0ZTZkIiwidXNlcl9pZCI6IjEifQ.t1brk8sk3JA9mN0wpOj1HSoGSIofdM68kV8ducT8zEM'
refresh = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3ODEwOTg1NiwiaWF0IjoxNzc4MDIzNDU2LCJqdGkiOiIxZWE1N2QyMTYzMTQ0YTNiYTY0MTU4MzA5MDdhZWQ1NiIsInVzZXJfaWQiOiIxIn0.i4pXk7Zw8x_TjjoGSPsEI04sNYIOKCHjoOm-EFG0HFg'


def criar_task_teste(dict_info:dict):

    response = requests.post("http://127.0.0.1:8000/api/v1/tasks/create/",
    data=dict_info,
    headers= {
        "Authorization": f"Bearer {access}"
    })

    print(response.ok, response.status_code)

    dados = response.json()

    return dados


def listar_task_teste():

    response = requests.get("http://127.0.0.1:8000/api/v1/tasks/",
    headers= {
        "Authorization": f"Bearer {access}"
    })

    print(response.ok, response.status_code)
    response.encoding = "utf-8"
    dados = response.json()

    return dados


def deletar_task_teste(pk:int):

    response = requests.post(f"http://127.0.0.1:8000/api/v1/tasks/delete/{pk}/",
    headers= {
        "Authorization": f"Bearer {access}"
    })

    print(response.ok, response.status_code)
    response.encoding = "utf-8"
    dados = response.json()

    return dados


def atualizar_task_teste(pk:int, update_info:dict):

    response = requests.patch(f"http://127.0.0.1:8000/api/v1/tasks/update/{pk}/",
    data=update_info
    ,headers= {
        "Authorization": f"Bearer {access}"
    })

    print(response.ok, response.status_code)
    response.encoding = "utf-8"
    dados = response.json()

    return dados


def deletar_task_teste(pk: int):
    response = requests.delete(f"http://127.0.0.1:8000/api/v1/tasks/delete/{pk}/",
    headers= {
        "Authorization": f"Bearer {access}"
    })

    print(response.ok, response.status_code)
    

if __name__ == "__main__":

    from datetime import datetime

    data = datetime.strptime("23/05/2026 20:55", "%d/%m/%Y %H:%M")
    print(data)

    # dados = atualizar_task_teste(1, {
    #     "data_conclusao": data
    # })

    # da = deletar_task_teste(5)

    # print(da)

    # print(gerar_tokens_acesso(username="admin", password="123"))


    print(listar_task_teste())
    
    # data = {
    #     "refresh": refresh
    # }

    # response = requests.post("http://127.0.0.1:8000/api/v1/token/refresh/", data=data)

    # dados = response.json()

    # print(dados)

