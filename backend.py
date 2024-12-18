# Importações
import mysql.connector as mysql
from mysql.connector import Error
from flask import Flask, request, jsonify


# Confifuração
app = Flask(__name__)

cred = {"host": "localhost",
        "user": "root",
        "password": "",
        "database": "apirest"}

conex = mysql.connect(**cred)


# Funções
## Retornar produtos e SKUs
@app.route("/produtos", methods = ["GET"])
def retornarProdutos():
    try:
        ### Consulta
        cursor = conex.cursor()
        
        cursor.execute("select nome_externo as Nome, nome as Caracteristicas, estoque as Disponibilidade, preco_tab as Preço, preco_lis as Preço_com_Desconto from produto join sku on produto.id = sku.id_produto;")
        
        prods = cursor.fetchall()
        
        headers = [desc[0] for desc in cursor.description]

        ### Retorno
        return jsonify({"mensagem": "Lista de produtos:",
                        "headers": headers,
                        "dados": prods}), 200
    except Error:
        return jsonify({"mensagem": "Não foi possível gerar uma lista de produtos!"}), 500
    
    
## Cadastrar produto
@app.route("/produtos", methods = ["POST"])
def criarProduto():
    try:
        dados = request.json
        
        ### Criando produto
        int = dados.get("nome_interno") 
        ext = dados.get("nome_externo")
        desc = dados.get("descricao")
        fab = dados.get("fabricante")
        atv = dados.get("ativo")
        
        cursor = conex.cursor()
        
        cursor.execute(f'insert into produto values(0, "{int}", "{ext}", "{desc}", "{fab}", "{atv}");')
        
        conex.commit()
        
        ### Criando sku, se aplicável
        sku = dados.get("sku")

        if(sku != ""):
            for loop in sku:
                cod = loop.get("cod")
                nome = loop.get("nome")
                est = loop.get("estoque")
                tab = loop.get("preco_tab")
                lis = loop.get("preco_lis")
                
                cursor.execute(f'insert into sku values(0, "{cod}", "{nome}", "{est}", "{tab}", "{lis}", (select id from produto order by id desc limit 1));')
            
            conex.commit()
        
        ### Retorno
        return jsonify({"mensagem": "Produto cadastrado com sucesso!"}), 200
    except Error as e:
        return jsonify({"mensagem": "Falha ao cadastrar produto!"}), 500


## Retornar um produto específico
@app.route("/produtos/:id", methods = ["GET"])
def retornarProduto():   
    try:
        ### Consulta
        cursor = conex.cursor()
        
        cursor.execute(f'select nome_externo as Nome, nome as Caracteristicas, estoque as Disponibilidade, preco_tab as Preço, preco_lis as Preço_com_Desconto from produto join sku on produto.id = sku.id_produto where produto.id = (select id from produto order by id desc limit 1)')
    
        prod = cursor.fetchall()
        
        headers = [desc[0] for desc in cursor.description]

        ### Retorno
        return jsonify({"mensagem": "Produto:",
                        "headers": headers,
                        "dados": prod}), 200
    except Error:
        return jsonify({"mensagem": "Não foi possível carregar o produto!"}), 500


## Atualizar produto e SKU
@app.route("/produtos/:id", methods = ["PATCH"])
def atualizarProduto():
    dados = request.json
    
    try:
        cursor = conex.cursor()
        
        ### Atualizando produto
        for chave, valor in dados.items():
            if(chave == "sku"):
                continue
            else:
                cursor.execute(f'update produto set {chave} = "{valor}" where id = (select id from (select id from produto order by id desc limit 1) as subquery)')
        
        ### Atualizando SKU, se aplicável
        if("sku" in dados.keys()):
            for c, v in dados["sku"].items():
                if(c == "cod"):
                    continue
                
                cursor.execute(f'update sku set {c} = {v} where cod = {valor["cod"]}')
                
        ### Retorno
        return jsonify({"mensagem": "Produto atualizado!"}), 200
    except Error:
        return jsonify({"mensagem": "Não foi possível atualizar o produto!"}), 500


## Deletar produto e SKU
@app.route("/produtos/:id", methods = ["DELETE"])
def deletarProduto():
    try:
        ### Deletando o produto e seus SKUs
        cursor = conex.cursor()
        
        cursor.execute(f'delete from sku where id_produto = (select id from produto order by id desc limit 1)')
        
        conex.commit()
        
        cursor.execute(f'delete from produto where id = (select id from (select id from produto order by id desc limit 1) as subquery)')
        
        conex.commit()

        ### Retorno
        return jsonify({"mensagem": "Produto deletado!"}), 200
    
    except Error:
        return jsonify({"mensagem": "Não foi possível deletar o produto!"}), 500
    
    
# Main
if(__name__ == '__main__'):
    app.run()