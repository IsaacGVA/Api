from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899
    }
]

@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
    return {"erro": "Livro não encontrado"}, 404

@app.route('/livros', methods=['POST'])
def criar_livro():
    dados = request.get_json()

    if not dados.get('titulo') or not dados.get('autor'):
        return {"erro": "Título e autor são obrigatórios"}, 400

    if dados.get('ano') is None or dados['ano'] < 0:
        return {"erro": "Ano inválido"}, 400

    for l in livros:
        if l['titulo'].lower() == dados['titulo'].lower():
            return {"erro": "Livro já cadastrado"}, 400

    novo = {
        "id": len(livros) + 1,
        "titulo": dados['titulo'],
        "autor": dados['autor'],
        "ano": dados['ano']
    }

    livros.append(novo)

    return {
        "mensagem": "Livro cadastrado com sucesso",
        "livro": novo
    }, 201

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    dados = request.get_json()

    for livro in livros:
        if livro['id'] == id:

            if dados.get('titulo'):
                livro['titulo'] = dados['titulo']

            if dados.get('autor'):
                livro['autor'] = dados['autor']

            if dados.get('ano') is not None:
                if dados['ano'] < 0:
                    return {"erro": "Ano inválido"}, 400
                livro['ano'] = dados['ano']

            return {
                "mensagem": "Livro atualizado com sucesso",
                "livro": livro
            }

    return {"erro": "Livro não encontrado"}, 404

@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return {"mensagem": "Livro removido com sucesso"}

    return {"erro": "Livro não encontrado"}, 404

if __name__ == '__main__':
    app.run(debug=True)