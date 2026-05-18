from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = [
    {
        "nome": "Ana",
        "email": "ana@gmail.com",
        "telefone": "(14) 99999-1111"
    },
    {
        "nome": "Carlos",
        "email": "carlos@gmail.com",
        "telefone": "(14) 98888-2222"
    },
    {
        "nome": "Julia",
        "email": "julia@gmail.com",
        "telefone": "(14) 97777-3333"
    }
]

@app.route("/usuarios")
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)