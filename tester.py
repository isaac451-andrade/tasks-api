import requests

def gerar_tokens_acesso(username: str, password: str):
    data = {
        "username": username.strip(),
        "password": password.strip()
    }

    response = requests.post("http://127.0.0.1:8000/api/v1/token/", data=data)

    dados = response.json()

    return dados


access = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3OTUwMDgxLCJpYXQiOjE3Nzc5NDY0ODEsImp0aSI6ImI2NDJjMWEzMDJhMDRmYjRhMDNkNTU2YTM5MmFhOGYxIiwidXNlcl9pZCI6IjEifQ.0_bfbYeFtc_98v-p_e23oxyk6RyedYK8oryU7yMtdPs'
refresh = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3ODAzMTg2OSwiaWF0IjoxNzc3OTQ1NDY5LCJqdGkiOiIxZjdhNGRhYjQwNTg0YTZkOGQ3YjZmNWE5ZWI1ZDg2MyIsInVzZXJfaWQiOiIxIn0.Q1AR-d1j6lL4aa92NwWBSJIgS_S2BDi_wQMP9Uij0oI'


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

if __name__ == "__main__":
    print(atualizar_task_teste(1, {
        "titulo": "AAAAAAAAAA",
        "descricao": "BBBBBBBBBBBB"
    }))

    print(listar_task_teste());
    
    # data = {
    #     "refresh": refresh
    # }

    # response = requests.post("http://127.0.0.1:8000/api/v1/token/refresh/", data=data)

    # dados = response.json()

    # print(dados)
