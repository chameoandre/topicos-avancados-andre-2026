# Manual do Professor: Conectividade e Monitoramento (Roteiro 06)

Este guia serve como referência rápida para configurar o ambiente do **Porto Central** antes do início das aulas, garantindo o acesso dos alunos e a supervisão do tráfego.

## 1. Pré-requisitos (Configuração NAT no VirtualBox)

Para que o servidor Linux (VM) seja acessível pelo Mac (Host), certifique-se de que a VM está em modo **NAT** com as seguintes regras de **Redirecionamento de Portas** (Port Forwarding):

| Nome | Protocolo | IP Hospedeiro | Porta Hospedeiro | IP Convidado | Porta Convidado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ssh** | TCP | `127.0.0.1` | `2222` | (vazio) | `22` |
| **vscode** | TCP | `127.0.0.1` | `8080` | (vazio) | `8080` |

---

## 2. Passo a Passo de Inicialização

Siga esta sequência exata no terminal do seu Mac:

### Passo A: Estabelecer Conexão SSH e Túnel de Monitoramento
Abra o terminal do Mac e conecte-se à VM puxando o painel do Ngrok para a sua máquina local:
```bash
ssh -L 4040:127.0.0.1:4040 ifsc@127.0.0.1 -p 2222
```

### Passo B: Iniciar o Túnel Público (Ngrok)
Dentro do terminal SSH (já logado na VM), inicie o túnel usando o seu domínio estático reservado:
```bash
ngrok http --domain=wobbly-subscript-onshore.ngrok-free.dev 8080
```

---

## 3. Como Supervisionar a Aula

### Acesso dos Alunos
Os alunos devem acessar a URL fixa via navegador (Chrome/Edge):
👉 **`https://wobbly-subscript-onshore.ngrok-free.dev`**

### Monitoramento do Professor (Traffic Inspection)
Para ver em tempo real **quais arquivos os alunos estão acessando**, erros de requisição e caminhos percorridos, abra no navegador do seu **Mac**:
👉 **`http://localhost:4040`**

> [!TIP]
> No painel do Ngrok (porta 4040), você consegue ver o histórico de todas as requisições HTTP. Se um aluno estiver com erro no código, você verá a requisição falhando (status 404 ou 500) ali na hora!

---

## 4. Troubleshooting Rápido

*   **SSH falhou (Connection Refused):** Verifique se a VM está ligada e se a porta 2222 está configurada no VirtualBox.
*   **Ngrok não inicia:** Verifique se o token de autenticação foi adicionado (`ngrok config add-authtoken ...`).
*   **Página não carrega para alunos:** Verifique se o serviço do VS Code está rodando na VM (`sudo systemctl status code-server@ifsc`).
