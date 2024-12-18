# Importações
import requests
from tabulate import tabulate


# Main
## Tiago: Quero visualizar todos os produtos que possuo cadastrado.
url = "http://127.0.0.1:5000/produtos"

try:
    result = requests.get(url)
    
    ### Exibição    
    print(result.json()["mensagem"])
    print(tabulate(result.json()["dados"], headers=result.json()["headers"], tablefmt="grid"))
    print("")

except requests.exceptions.RequestException as e:
    print(e)


## Tiago: Quero cadastrar um novo produto para vender.
url = "http://127.0.0.1:5000/produtos"

dados = {"nome_interno" : "suco",
         "nome_externo" : "Suc",
         "descricao" : "Refresco saudável saborizado",
         "fabricante" : "Dell Valle",
         "ativo" : "1",
         
         "sku": [
                {"cod": "2441258000226", "nome": "MOR-5ML", "estoque": 34, "preco_tab": 8.70, "preco_lis": 6.80},
                {"cod": "2441258000233", "nome": "MOR-10ML", "estoque": 18, "preco_tab": 12.20, "preco_lis": 10.99},
                {"cod": "2441258000240", "nome": "MOR-20ML", "estoque": 10, "preco_tab": 18.50, "preco_lis": 15.12},
                {"cod": "2441258000257", "nome": "LM-5ML", "estoque": 31, "preco_tab": 8.70, "preco_lis": 6.80},
                {"cod": "2441258000264", "nome": "LM-10ML", "estoque": 20, "preco_tab": 12.20, "preco_lis": 10.99},
                {"cod": "2441258000271", "nome": "LM-20ML", "estoque": 7, "preco_tab": 18.50, "preco_lis": 15.12},
                {"cod": "2441258000288", "nome": "UV-5ML", "estoque": 29, "preco_tab": 8.70, "preco_lis": 6.80},
                {"cod": "2441258000295", "nome": "UV-10ML", "estoque": 17, "preco_tab": 12.20, "preco_lis": 10.99},
                {"cod": "2441258000301", "nome": "UV-20ML", "estoque": 6, "preco_tab": 18.50, "preco_lis": 15.12},
            ]
         }

try:
    ### Requisição
    result = requests.post(url, json = dados)
    
    ### Retorno
    print(result.json()["mensagem"])
    print("")

except requests.exceptions.RequestException as e:
    print(e)


## Tiago: Quero visualizar as informações do produto que acabei de cadastrar.
url = "http://127.0.0.1:5000/produtos/:id"

try:
    result = requests.get(url)
    
    ### Exibição    
    print(result.json()["mensagem"])
    print(tabulate(result.json()["dados"], headers=result.json()["headers"], tablefmt="grid"))
    print("")

except requests.exceptions.RequestException as e:
    print(e)


## Tiago: Percebi que escrevi por acidente o nome errado no produto e coloquei a o estoque errado na garrafa de 500ml de morango.
url = "http://127.0.0.1:5000/produtos/:id"

dados = {"nome_externo" : "Suco",
    
         "sku" : {"cod" : 2441258000226,
                  "estoque" : 43}
         }

try:
    result = requests.patch(url, json = dados)
    
    print(result.json()["mensagem"])
    print("")
    
except requests.exceptions.RequestException as e:
     print(e)
     
     
## Visualizar PATCH
url = "http://127.0.0.1:5000/produtos/:id"

try:
    result = requests.get(url)
    
    ### Exibição    
    print(result.json()["mensagem"])
    print(tabulate(result.json()["dados"], headers=result.json()["headers"], tablefmt="grid"))
    print("")

except requests.exceptions.RequestException as e:
    print(e)
    

## Tiago: Não vou mais vender esse produto, vou deletar.
url = "http://127.0.0.1:5000/produtos/:id"

try:
    result = requests.delete(url)

    print(result.json()["mensagem"])
    print("")

except requests.exceptions.RequestException as e:
     print(e)


## Visualização Final
url = "http://127.0.0.1:5000/produtos"

try:
    result = requests.get(url)
    
    ### Exibição    
    print(result.json()["mensagem"])
    print(tabulate(result.json()["dados"], headers=result.json()["headers"], tablefmt="grid"))
    print("")

except requests.exceptions.RequestException as e:
    print(e)