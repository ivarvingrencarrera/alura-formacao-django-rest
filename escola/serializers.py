from rest_framework import serializers

from escola.models import Aluno, Curso, Matricula


class AlunoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
    

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []