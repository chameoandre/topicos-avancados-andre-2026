def apresentar(nome, idade):
    return f"Olá, meu nome é {nome} e tenho {idade} anos."


def maior_de_idade(idade):
    return idade >= 18

alunos = [
    {"nome": "João", "idade": 17},
    {"nome": "Maria", "idade": 16},
    {"nome": "Carlos", "idade": 18},
    {"nome": "Fernanda", "idade": 19},

]



for aluno in alunos:
    print(apresentar(aluno["nome"], aluno["idade"]))

    if maior_de_idade(aluno["idade"]):
        print(f"{aluno['nome']} é maior de idade.")