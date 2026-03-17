def apresentar(nome, idade):
    return f"Olá, meu nome é {nome} e tenho {idade} anos."

def maior_de_idade(idade):
    return idade >= 18

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def verificar_aprovacao(notas):
    media = calcular_media(notas)
    return media >= 7

def adicionar_nota(aluno, nota):
    aluno["notas"].append(nota)

alunos = [
    {"nome": "João", "idade": 17, "notas": [6, 7, 8]},
    {"nome": "Maria", "idade": 16, "notas": [5, 6, 7]},
    {"nome": "Carlos", "idade": 18, "notas": [8, 9, 10]},
]

for aluno in alunos:
    print(apresentar(aluno["nome"], aluno["idade"]))
    if maior_de_idade(aluno["idade"]):
        print("É maior de idade.")
    else:
        print("É menor de idade.")

    media = calcular_media(aluno["notas"])
    print(f"Média das notas: {media}")

    if verificar_aprovacao(aluno["notas"]):
        print("Aprovado!")
    else:
        print("Reprovado!")
    print("-" * 20)


