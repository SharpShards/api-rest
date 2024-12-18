# Banco de Dados
Banco de dados relacional desenvolvido em MySQL, contendo as tabelas e dados necessários para o funcionamento da API.

## Estrutura
### Produto
1. `id`: Identificador único para cada produto.
2. `nome_interno`: Slug manipulado pelo sistema.
3. `nome_externo`: Nome exibido para os clientes.
4. `descricao`: Característiacs do produto.
5. `fabricante`: Empresa responsável pela produção.
6. `ativo`: Disponibilidade do produto para venda.

| id | nome_interno | nome_externo | descricao | fabricante | ativo |
| ----- | ------- | ------ | ----- | ----- | --------- |
| 1 | coca-cola | Coca-Cola | Refrigerante carbonato | The Coca Cola Company | 1 |
| 2 | fanta | Fanta | Refrigerante de sabores variados | The Coca Cola Company | 1 |
| ... | ... | ... | ... | ... | ... |

### SKU
1. `id`: Identificador único para cada SKU.
2. `cod`: Código EAN-13 de identificação do produto e sua variação.
3. `nome`: Nome descritivo.
4. `estoque`: Quantidade disponível.
5. `preco_tab`: Preço original.
6. `preco_lis`: Preço com desconto.
7. `id_produto`: Identificador do produto ao qual o SKU se refere.

| id | cod | nome | estoque | preco_tab | preco_lis | id_produto |
| -- | ------- | ------ | ----- | ----- | ------ | --------- |
| 1 | 1530578000090 | CC-2ML-NOR | 87 | 7.50 | 5.20 | 1
| 2 | 1530578000094 | CC-2ML-ZER | 65 | 7.50 | 5.20 | 1
| ... | ... | ... | ... | ... | ... |

## Importação
O arquivo `data.sql` contém os dados de exemplo utilizados na simulação de uso da API.

Para importar o arquivo, utilize o PHPMyAdmin ou o MySQL, e altere as credenciais no arquivo `backend.py`, se necessário. Após a importação, o sistema estará pronto para uso.
