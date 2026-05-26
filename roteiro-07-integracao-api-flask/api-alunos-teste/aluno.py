class Aluno:
    contador = 1  # Contador para gerar IDs únicos para cada aluno

    # Método construtor para inicializar os atributos do aluno
    def __init__(self, nome, idade):
        self.id = Aluno.contador
        self.nome = nome
        self.idade = idade
        self.notas = []
        Aluno.contador += 1

    # Método para adicionar uma nota ao aluno
    def adicionar_nota(self, nota):
        self.notas.append(nota)

    # Método para calcular a média das notas do aluno
    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    # Método para verificar se o aluno foi aprovado (média >= 7)
    def aprovado(self):
        return self.calcular_media() >= 7

    # Método para converter o objeto Aluno em um dicionário, facilitando a conversão para JSON
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "notas": self.notas,
            "media": self.calcular_media(),
            "aprovado": self.aprovado(),
        }
