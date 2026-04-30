# Guia de Revisão: Avaliação Teórica 01 (Tópicos Avançados)

Este documento sintetiza os conceitos fundamentais abordados do Roteiro 01 ao Roteiro 07, servindo como base de estudos para a primeira avaliação teórica da Unidade Curricular.

---

## 1. Versionamento de Código (Git & GitHub)

O Git é um sistema de controle de versão distribuído que permite rastrear alterações no código-fonte.

*   **Repositório:** Local onde o projeto e seu histórico de alterações são armazenados.
*   **Commit:** "Fotografia" do estado atual do código. Cada commit possui uma mensagem descritiva.
*   **Push:** Envia os commits locais para o servidor remoto (GitHub).
*   **Pull:** Traz as alterações do servidor remoto para a máquina local.
*   **Clone:** Cria uma cópia local de um repositório remoto pela primeira vez.

---

## 2. Orientação a Objetos em Python

A OO permite organizar o código simulando objetos do mundo real.

*   **Classe:** É o "molde" ou "planta baixa" (ex: Classe `Carro`).
*   **Objeto:** É a instância real da classe (ex: Meu carro placa ABC-1234).
*   **Atributos:** Características do objeto (ex: `cor`, `modelo`).
*   **Métodos:** Ações que o objeto pode realizar (ex: `acelerar()`, `frear()`).
*   **Construtor (`__init__`):** Método especial executado automaticamente ao criar um novo objeto para inicializar seus atributos.

---

## 3. Desenvolvimento Web com Flask

O Flask é um micro-framework Python para criação de aplicações web.

*   **Rotas (`@app.route`):** Definem qual URL aciona qual função no Python.
*   **Templates (Jinja2):** Permitem criar páginas HTML dinâmicas.
    *   `{{ variavel }}`: Exibe o conteúdo de uma variável.
    *   `{% for item in lista %}`: Estrutura de repetição para gerar listas no HTML.
*   **Métodos HTTP:**
    *   **GET:** Usado para solicitar dados (ex: acessar uma página). Os dados aparecem na URL.
    *   **POST:** Usado para enviar dados (ex: formulários de cadastro). Mais seguro, dados vão no "corpo" da requisição.
*   **Request Form:** Forma de capturar os dados enviados pelo usuário via formulário no backend Python.

---

## 4. Docker e Virtualização

Tecnologia de empacotamento de software em unidades isoladas chamadas containers.

### Diferença Fundamental:
*   **Máquina Virtual (VM):** Simula um hardware completo, incluindo um sistema operacional inteiro (pesado).
*   **Container:** Compartilha o kernel do sistema operacional hospedeiro, isolando apenas a aplicação e suas bibliotecas (leve e rápido).

### Conceitos Docker:
*   **Imagem:** Arquivo estático (somente leitura) que contém o manual de instruções do container.
*   **Container:** A imagem em execução.
*   **Port Mapping (`-p hospedeiro:container`):** Mapeia uma porta da máquina real para dentro do container.
*   **Volumes (`-v hospedeiro:container`):** Sincroniza uma pasta local com uma pasta dentro do container (persistência).

---

## 5. Dockerfile e Docker Compose

*   **Dockerfile:** Arquivo de "receita" para criar sua própria imagem customizada.
    *   `FROM`: Define a imagem base (ex: `python:3.11`).
    *   `WORKDIR`: Define a pasta de trabalho dentro do container.
    *   `COPY`: Copia arquivos do seu computador para o container.
    *   `RUN`: Executa comandos de instalação (ex: `pip install`).
    *   `CMD`: Comando que inicia a aplicação ao subir o container.

*   **Docker Compose:** Ferramenta para orquestrar múltiplos containers (ex: Web + Banco de Dados) usando um único arquivo `.yml`.
    *   Permite subir toda a infraestrutura com `docker-compose up -d`.
