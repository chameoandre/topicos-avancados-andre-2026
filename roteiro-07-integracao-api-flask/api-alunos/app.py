from flask import Flask, jsonify, request, render_template
from aluno import Aluno

app = Flask(__name__)

# Banco de dados simulado em memória
alunos = []

# Inicializando com alguns dados de teste
aluno1 = Aluno("João Silva", 17)
aluno1.adicionar_nota(8.5)
aluno2 = Aluno("Maria Souza", 16)
aluno2.adicionar_nota(9.0)

alunos.append(aluno1)
alunos.append(aluno2)

# ==========================================
# 1. ROTA DE TELA (HTML Estático)
# ==========================================
@app.route("/", methods=["GET"])
def pagina_inicial():
    # Retorna o arquivo HTML sem injetar dados via Jinja2
    return render_template("index.html")

# ==========================================
# 2. ROTAS DE API (Endpoints JSON)
# ==========================================

# ROTA A: Listar Alunos (GET)
@app.route("/api/alunos", methods=["GET"])
def listar_alunos():
    # Converte a lista de objetos Aluno para uma lista de dicionários usando o método to_dict()
    alunos_dict = [aluno.to_dict() for aluno in alunos]
    return jsonify(alunos_dict), 200

# ROTA B: Adicionar um novo aluno (POST)
@app.route("/api/alunos", methods=["POST"])
def adicionar_aluno():
    # Extrai os dados do corpo da requisição JSON
    dados = request.get_json()
    nome = dados.get("nome")
    idade = dados.get("idade")

    # Valida os dados recebidos
    if not nome or not isinstance(idade, int):
        return jsonify({"error": "Dados inválidos. 'nome' deve ser uma string e 'idade' deve ser um inteiro."}), 400

    # Cria um novo objeto Aluno e adiciona à lista de alunos
    novo_aluno = Aluno(nome, idade)
    alunos.append(novo_aluno)

    return jsonify(novo_aluno.to_dict()), 201

# ROTA C: Remover Aluno (DELETE)
@app.route("/api/alunos/<int:id>", methods=["DELETE"])
def api_remover_aluno(id):
    global alunos
    # Verifica se o aluno existe
    aluno_existe = any(aluno.id == id for aluno in alunos)
    
    if not aluno_existe:
        return jsonify({"erro": "Aluno não encontrado"}), 404
        
    # Remove o aluno da lista
    alunos = [aluno for aluno in alunos if aluno.id != id]
    return jsonify({"mensagem": f"Aluno {id} removido com sucesso"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
