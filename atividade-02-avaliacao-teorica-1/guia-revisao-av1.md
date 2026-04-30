# Guia de Revisão: Avaliação Teórica 01 (Tópicos Avançados)

Este documento sintetiza os conceitos fundamentais abordados do Roteiro 01 ao Roteiro 07, servindo como base de estudos para a primeira avaliação teórica da Unidade Curricular.

---

## 0. Por que estudamos isso? (Contexto Profissional)

Nesta unidade curricular, estamos simulando o **Pipeline de Desenvolvimento Moderno**. 
*   **Git/GitHub:** No mercado, ninguém trabalha sozinho. O Git garante que o código não se perca e que vários desenvolvedores trabalhem no mesmo projeto.
*   **Flask & Python OO:** O Python é uma das linguagens mais usadas no mundo (IA, Dados e Web). O Flask nos permite transformar lógica pura em serviços acessíveis via navegador.
*   **Docker & Containers:** É o padrão atual da indústria (DevOps). Antigamente, o software funcionava na máquina do desenvolvedor, mas dava erro no servidor ("Na minha máquina funciona!"). O Docker resolve isso empacotando tudo o que o app precisa para rodar em qualquer lugar.

---

## 1. Versionamento de Código (Git & GitHub)

O Git rastreia alterações. O GitHub hospeda o código na nuvem.

### Comandos Essenciais:
*   `git init`: Inicia um repositório novo.
*   `git status`: **Fundamental.** Mostra quais arquivos foram modificados e o que ainda não foi adicionado.
*   `git add <arquivo>` ou `git add .`: Prepara os arquivos para o commit.
*   `git commit -m "mensagem"`: Grava as alterações com uma justificativa.
*   `git log --oneline`: Mostra o histórico resumido de quem fez o quê.
*   `git push origin main`: Envia seu trabalho para o GitHub.

---

## 2. Orientação a Objetos em Python

A OO permite organizar o código simulando objetos do mundo real.

### Exemplo Prático:
```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome      # Atributo
        self.preco = preco    # Atributo

    def exibir_detalhes(self): # Método
        print(f"Produto: {self.nome} - R$ {self.preco}")

# Criando um Objeto (Instanciando)
p1 = Produto("Mouse Gamer", 150.00)
p1.exibir_detalhes()
```

---

## 3. Desenvolvimento Web com Flask

Transforma o Python em um servidor que responde a requisições do navegador.

### Fluxo de uma Rota:
```python
@app.route('/saudacao/<nome>')
def saudacao(nome):
    # O Python processa a lógica e envia para o Template HTML
    return render_template('index.html', nome_usuario=nome)
```

### Métodos HTTP:
*   **GET:** Solicita a página (ex: digitar a URL).
*   **POST:** Envia dados sensíveis (ex: senhas, cadastros) através do `request.form`.

---

## 4. Docker e Virtualização

Isolamento de processos para garantir que o ambiente seja o mesmo em qualquer computador.

### Comandos de Inspeção e Monitoramento:
*   `docker ps`: Lista containers ativos.
*   `docker ps -a`: Lista todos (até os que deram erro e pararam).
*   `docker logs <nome>`: **Crucial.** Mostra o que está acontecendo "dentro" do container (erros do Python aparecem aqui).
*   `docker exec -it <nome> bash`: Entra no terminal de dentro do container para investigar arquivos.
*   `docker stop $(docker ps -q)`: Para todos os containers de uma vez.

---

## 5. Dockerfile e Docker Compose

*   **Dockerfile:** A "receita" de como montar o container.
    *   `FROM python:3.11-slim`: Escolhe uma base leve.
    *   `COPY . .`: Copia todo o seu projeto para dentro do container.

*   **Docker Compose:** O "Guindaste" que sobe vários containers.
    *   `docker-compose up -d`: Sobe tudo em segundo plano.
    *   `docker-compose down`: Para e **remove** todos os containers e redes criadas pelo arquivo `.yml`.
    *   `docker-compose logs -f`: Acompanha os logs de todos os serviços (Web e Banco) simultaneamente.
