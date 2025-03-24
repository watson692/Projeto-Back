from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista estática de filmes
filmes = [
    {"id": 1, "titulo": "O Poderoso Chefão", "descricao": "Um épico sobre a máfia italiana nos EUA."},
    {"id": 2, "titulo": "Interestelar", "descricao": "Uma jornada espacial em busca de um novo lar para a humanidade."},
    {"id": 3, "titulo": "Matrix", "descricao": "Um hacker descobre a verdade sobre a realidade."}
]

print("Iniciando o servidor Flask...")

@app.route('/')
def home():
    print("Rota '/' acessada")
    return jsonify({"mensagem": "Servidor Flask rodando na porta 5000!"})

# Endpoint para listar todos os filmes
@app.route('/filmes', methods=['GET'])
def listar_filmes():
    print("Rota '/filmes' acessada")
    return jsonify(filmes)

# Endpoint para adicionar um novo filme
@app.route('/filmes', methods=['POST'])
def adicionar_filme():
    novo_filme = request.get_json()
    if not novo_filme.get("id") or not novo_filme.get("titulo") or not novo_filme.get("descricao"):
        return jsonify({"erro": "Todos os campos (id, titulo, descricao) são obrigatórios"}), 400

    filmes.append(novo_filme)
    return jsonify(novo_filme), 201

# Endpoint para obter um filme pelo ID
@app.route('/filmes/<int:filme_id>', methods=['GET'])
def obter_filme(filme_id):
    filme = next((f for f in filmes if f["id"] == filme_id), None)
    if filme:
        return jsonify(filme)
    return jsonify({"erro": "Filme não encontrado"}), 404

# Endpoint para atualizar um filme pelo ID
@app.route('/filmes/<int:filme_id>', methods=['PUT'])
def atualizar_filme(filme_id):
    filme = next((f for f in filmes if f["id"] == filme_id), None)
    if not filme:
        return jsonify({"erro": "Filme não encontrado"}), 404

    dados = request.get_json()
    filme.update(dados)
    return jsonify(filme)

# Endpoint para deletar um filme pelo ID
@app.route('/filmes/<int:filme_id>', methods=['DELETE'])
def deletar_filme(filme_id):
    global filmes
    filmes = [f for f in filmes if f["id"] != filme_id]
    return jsonify({"mensagem": "Filme removido com sucesso"}), 200

if __name__ == '__main__':
    print("Executando o aplicativo Flask...")
    app.run(host='localhost', port=5000, debug=True)
