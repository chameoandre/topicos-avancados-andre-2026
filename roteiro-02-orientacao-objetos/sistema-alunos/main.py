from aluno import Aluno

alunos = [
    Aluno("João", 17),
    Aluno("Maria", 16),
    Aluno("Carlos", 18),
]


alunos[0].adicionar_nota(6)
alunos[0].adicionar_nota(7)
alunos[0].adicionar_nota(8)

alunos[1].adicionar_nota(5)
alunos[1].adicionar_nota(6)
alunos[1].adicionar_nota(7)

alunos[2].adicionar_nota(8)
alunos[2].adicionar_nota(9)
alunos[2].adicionar_nota(10)


for aluno in alunos:
    print(aluno.apresentar())
    print("Média: ", aluno.calcular_media())
    
    if aluno.aprovado():
        print("Aprovado!")
    else:
        print("Reprovado!")
    print("-" * 20)
