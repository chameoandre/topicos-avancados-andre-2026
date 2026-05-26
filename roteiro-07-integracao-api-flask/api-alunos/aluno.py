class Aluno:
    contador = 1  # Contador estático para gerar IDs únicos

    def __init__(self, nome, idade):
        self.id = Aluno.contador
        self.nome = nome
        self.idade = idade
        self.notas = []
        Aluno.contador += 1

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprovado(self):
        return self.calcular_media() >= 7

    # Método crucial que transforma o objeto em um Dicionário Python 
    # que o Flask consegue converter em formato JSON (texto bruto)
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "media": self.calcular_media(),
            "aprovado": self.aprovado(),
        }
