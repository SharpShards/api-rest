# Importações
import requests


# Main

## Tiago: Quero cadastrar um novo produto para vender.
url = "http://127.0.0.1:5000/produtos"

dados = {"nome_interno" : "sprite",
         "nome_externo" : "Sprite",
         "descricao" : "Refrigerante de limão",
         "fabricante" : "The Coca-Cola Company",
         "ativo" : "1",
         
         "sku": [
                {"cod": "1530578000040", "nome": "SP-2ML-NOR", "estoque": 115, "preco_tab": 4.50, "preco_lis": 2.80, "id_produto": 9},
                {"cod": "1530578000052", "nome": "SP-5ML-NOR", "estoque": 75, "preco_tab": 4.50, "preco_lis": 2.80, "id_produto": 9},
                {"cod": "1530578000069", "nome": "SP-10ML-NOR", "estoque": 20, "preco_tab": 4.50, "preco_lis": 2.80, "id_produto": 9},
                {"cod": "1530578000106", "nome": "SP-2ML-ZER", "estoque": 92, "preco_tab": 4.50, "preco_lis": 2.80, "id_produto": 9},
                {"cod": "1530578000113", "nome": "SP-5ML-ZER", "estoque": 51, "preco_tab": 4.50, "preco_lis": 2.80, "id_produto": 9},
                {"cod": "1530578000120", "nome": "SP-10ML-ZER", "estoque": 7, "preco_tab": 4.50, "preco_lis": 2.80, "id_produto": 9},
            ]
         }

try:
    result = requests.post(url, json = dados)
    
    print(result.json()["mensagem"])

except requests.exceptions.RequestException as e:
    print(e)
    

## Tiago: Quero visualizar todos os produtos que possuo cadastrado.
url = "http://127.0.0.1:5000/produtos"

try:
    result = requests.get(url)
    
    print(result.json()["mensagem"])

except requests.exceptions.RequestException as e:
    print(e)


## Tiago: Quero visualizar as informações da Sprite.
url = "http://127.0.0.1:5000/produtos/:id"
id = 9

try:
    result = requests.get(url, json = id)
    
    print(result.json()["mensagem"])

except requests.exceptions.RequestException as e:
    print(e)


## Tiago: Quero alterar o nome da Sprite, que está com erro ortográfico, e alterar o estoque da garrafa de 500ml zero.
url = "http://127.0.0.1:5000/produtos/:id"

dados = {"id" : 9,
         "nome_externo" : "Sprite",
         
         "sku" : {"cod" : 1530578000113,
                  "estoque" : 51}
         }

try:
    result = requests.patch(url, json = dados)
    
    print(result.json()["mensagem"])
    
except requests.exceptions.RequestException as e:
     print(e)