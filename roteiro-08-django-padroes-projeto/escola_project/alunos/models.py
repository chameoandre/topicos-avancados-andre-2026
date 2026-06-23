from django.db import models

# Create your models here.


class Aluno(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    idade = models.IntegerField(verbose_name="Idade")
    nota = models.FloatField(default=0.0, verbose_name="Média")

    def aprovado(self):
        return self.nota >= 7.0

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "media": self.nota,
            "aprovado": self.aprovado(),
        }

    def __str__(self):
        return self.nome
