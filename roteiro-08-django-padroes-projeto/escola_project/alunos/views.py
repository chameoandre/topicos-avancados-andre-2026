from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Aluno


# Tela inicial (apresenta o index.html)
def pagina_inicial(request):
    return render(request, "index.html")


@csrf_exempt
def api_alunos(request):
    # GET: Listar todos os alunos
    if request.method == "GET":
        lista_alunos = Aluno.objects.all()
        dados = [aluno.to_dict() for aluno in lista_alunos]
        return JsonResponse(dados, safe=False)

    # POST: Criar um novo aluno
    elif request.method == "POST":
        payload = json.loads(request.body)
        nome = payload.get("nome")
        idade = payload.get("idade")
        nota = payload.get("media", 8.5)  # Valor padrão para nota

        if not nome or not isinstance(idade, int) or not isinstance(nota, (int, float)):
            return JsonResponse({"error": "Dados inválidos"}, status=400)

        aluno = Aluno.objects.create(nome=nome, idade=idade, nota=nota)
        return JsonResponse(aluno.to_dict(), status=201)


@csrf_exempt
def api_aluno_detalhe(request, id):
    # DELETE: Remover aluno pelo ID
    if request.method == "DELETE":
        try:
            aluno = Aluno.objects.get(id=id)
            aluno.delete()
            return JsonResponse({"message": "Aluno removido com sucesso"}, status=200)
        except Aluno.DoesNotExist:
            return JsonResponse({"error": "Aluno não encontrado"}, status=404)
