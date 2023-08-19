from rest_framework import viewsets, generics

from escola.models import Aluno, Curso, Matricula
from escola.serializers import AlunoSerializer, AlunoSerializerV2, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunosSerializer, ListaAlunosMatriculados
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    
    def get_serializer_class(self):
        return AlunoSerializerV2 if self.request.version == 'v2' else AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    def create(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(MatriculasViewSet, self).dispatch(*args, **kwargs)


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    serializer_class = ListaMatriculasAlunosSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    serializer_class = ListaAlunosMatriculados

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset