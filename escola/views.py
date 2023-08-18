from django.http import JsonResponse, HttpRequest

def alunos(request: HttpRequest):
    if request.method == 'GET':
        aluno = {'id': 1, 'nome': 'Guilherme'}
        return JsonResponse(aluno)
