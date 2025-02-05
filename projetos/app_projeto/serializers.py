from rest_framework import serializers
from .models import Projeto, Equipe
from dataclasses import fields
from pyexpat import model


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'

class EquipeBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ['id', 'nome']

class ProjetoSerializer(serializers.ModelSerializer):
    equipe = EquipeBasicSerializer()

    class Meta:
        model = Projeto
        fields = ['id', 
                  'nome', 'dt_inicio', 'dt_final', 'equipe']
        
class ProjetoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'dt_inicio', 'dt_final', ]