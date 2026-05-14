from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


pessoas = [
    {
        "id": 1,
        "nome": "Dom Casmurro",
        "email": "Machado de Assis",
        "telefone": 1899
    }
]

@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    return jsonify(pessoas)

@app.route('/pessoas/<int:id>', methods=['GET'])
def obter_pessoa(id):
    for pessoa in pessoas:
        if pessoa['id'] == id:
            return jsonify(pessoa)
    return {"erro": "pessoa não encontrado"}, 404

@app.route('/pessoas', methods=['POST'])
def criar_pessoa():
    dados = request.get_json()

    if not dados.get('nome') or not dados.get('email'):
        return {"erro": "nome e email são obrigatórios"}, 400

    if dados.get('telefone') is None or dados['telefone'] < 0:
        return {"erro": "telefone inválido"}, 400

    for l in pessoas:
        if l['nome'].lower() == dados['nome'].lower():
            return {"erro": "pessoa já cadastrado"}, 400

    novo = {
        "id": len(pessoas) + 1,
        "nome": dados['nome'],
        "email": dados['email'],
        "telefone": dados['telefone']
    }

    pessoas.append(novo)

    return {
        "mensagem": "pessoa cadastrado com sucesso",
        "pessoa": novo
    }, 201

@app.route('/pessoas/<int:id>', methods=['PUT'])
def atualizar_pessoa(id):
    dados = request.get_json()

    for pessoa in pessoas:
        if pessoa['id'] == id:

            if dados.get('nome'):
                pessoa['nome'] = dados['nome']

            if dados.get('email'):
                pessoa['email'] = dados['email']

            if dados.get('telefone') is not None:
                if dados['telefone'] < 0:
                    return {"erro": "telefone inválido"}, 400
                pessoa['telefone'] = dados['telefone']

            return {
                "mensagem": "pessoa atualizado com sucesso",
                "pessoa": pessoa
            }

    return {"erro": "pessoa não encontrado"}, 404

@app.route('/pessoas/<int:id>', methods=['DELETE'])
def deletar_pessoa(id):
    for pessoa in pessoas:
        if pessoa['id'] == id:
            pessoas.remove(pessoa)
            return {"mensagem": "pessoa removido com sucesso"}

    return {"erro": "pessoa não encontrado"}, 404

if __name__ == '__main__':
    app.run(debug=True)