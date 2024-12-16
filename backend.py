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
                prod = loop.get("id_produto")
                
                cursor.execute(f'insert into sku values(0, "{cod}", "{nome}", "{est}", "{tab}", "{lis}", "{prod}");')
            
            conex.commit()
        
        return jsonify({"mensagem": "Produto cadastrado com sucesso!"}), 200
    except Error as e:
        return jsonify({"mensagem": "Falha ao cadastrar produto!"}), 500
    

# Main
if(__name__ == '__main__'):
    app.run()