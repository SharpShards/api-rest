# API REST
API REST desenvolvida em Python, integrando com MySQL para receber e processar requisições HTTP, visando o gerenciamento de produtos e SKUs.

Esse projeto é dividido em duas partes:
- API: Responsável pelos endpoints e pelo processamento das requisições recebidas. 
- Teste: Simula um exemplo prático em que um funcionário de supermercado interage com a API para alterar o banco de dados.

## Tecnologias
Para o desenvolvimento e manipulação desse projeto, foram utilizadas as seguintes tecnologias:
- Python
- MySQL
- Git

## Componentes
- `frontend.py`: Simulação de solicitação de requisição originada pelo frontend.
  
- `backend.py`: API que recebe as requisições e interage com o MySQL.
- `gerador_ean13.py`: Gera códigos EAN13 usados para preencher o banco de dados.
- `database`: Banco de dados manipulado pela API.
- `requirements.txt`: Lista de dependências necessárias.
- `README.md`: Documentação da API

## Simulação
- Em um terminal, execute o script `backend.py` para iniciar o servidor Flask.
- Em outro terminal, execute o script `frontend.py` para iniciar a simulação.
- Observe as respostas retornadas no terminal `frontend.py`.

## Dependências
 Utilize o comando abaixo para instalar as dependências:

`pip install -r requirements.txt`
