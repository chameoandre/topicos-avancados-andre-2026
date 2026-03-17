from aluno import Aluno

alunos = [
    Aluno("João", 17),
    Aluno("Maria", 16),
    Aluno("Carlos", 18)
]

for aluno in alunos:
    print(aluno.apresentar())
    if aluno.maior_de_idade():
        print(f"{aluno.nome} é maior de idade.")


