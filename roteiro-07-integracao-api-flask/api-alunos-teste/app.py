from flask import Flask, jsonify, request, render_template
from aluno import Aluno

app = Flask(__name__)


# Banco de Dados simulado em memória
alunos = []


# Inicializando com alguns dados de teste
aluno1 = Aluno("Alice", 20)
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(9)

aluno2 = Aluno("Maria Souza", 22)
aluno2.adicionar_nota(8.5)
aluno2.adicionar_nota(9)


alunos.append(aluno1)
alunos.append(aluno2)


# ==========================================
# 1. ROTA DE TELA (HTML Estático)
# ==========================================


@app.route("/", methods=["GET"])
# Rota para a página inicial, que renderiza um template HTML, sem a injeção de dados via Jinja2, ou seja, é uma página estática
def pagina_inicial():
    return render_template("index.html")


# ==========================================
# 2. ROTAS DE API (JSON Dinâmico)
# ==========================================


# ROTA A: Listar todos os alunos (GET)
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
        return (
            jsonify(
                {
                    "error": "Dados inválidos. 'nome' deve ser uma string e 'idade' deve ser um inteiro."
                }
            ),
            400,
        )

    # Cria um novo objeto Aluno e adiciona à lista de alunos
    novo_aluno = Aluno(nome, idade)
    alunos.append(novo_aluno)

    return jsonify(novo_aluno.to_dict()), 201


# ROTA C: Remover Aluno (Delete)
@app.route("/api/alunos/<int:aluno_id>", methods=["DELETE"])
def remover_aluno(aluno_id):
    global alunos

    # Verifica se o aluno com o ID fornecido existe na lista de alunos
    aluno_existe = any(aluno.id == aluno_id for aluno in alunos)

    # Se o aluno não existir, retorna um erro 404 com uma mensagem de erro em formato JSON
    if not aluno_existe:
        return jsonify({"error": "Aluno não encontrado."}), 404

    if not aluno_existe:
        return jsonify({"error": "Aluno não encontrado."}), 404

    # Remove o aluno da lista usando uma compreensão de lista para criar uma nova lista que exclui o aluno com o ID fornecido
    alunos = [aluno for aluno in alunos if aluno.id != aluno_id]

    # Retorna uma mensagem de sucesso em formato JSON indicando que o aluno foi removido com sucesso
    return jsonify({"message": f"Aluno com ID {aluno_id} removido com sucesso."}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

