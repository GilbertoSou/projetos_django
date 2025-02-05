from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Projeto(models.Model):
    nome = models.CharField(verbose_name='Título do Projeto', max_length=100, blank=False, null=False)
    descricao = models.CharField(verbose_name='Descrição', max_length=500, blank=False, null=False)
    dt_inicio =  models.DateField(verbose_name='Data de Início', blank=False, null=False)
    dt_final = models.DateField(verbose_name='Data de Término', blank=False, null=False)

    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, related_name='projetos', null=True, blank=True)
    
    def __str__(self):
        return f'{self.nome} - {self.dt_inicio} - {self.dt_final}'


class Equipe(models.Model):
    nome = models.CharField(verbose_name='Nome da Equipe', max_length=100, blank=False, null=False)
    ativa = models.BooleanField(verbose_name='Em atividade', default=True)
    
    def count_membros(self):
        return self.membros.count()
    
    def __str__(self):
        return f'{self.nome}'
        

GENERO_CHOICES = (('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'))

class Membro(models.Model):
    nome = models.CharField(verbose_name='Nome do Membro', max_length=150, blank=False, null=False)
    genero = models.CharField(max_length=1, default='O', choices=GENERO_CHOICES)

    telefone = models.CharField(max_length=15, help_text='(99) 99999-9999', validators=[RegexValidator(regex=r'^\(\d{2}\) \d{5}-\d{4}$', 
                                 message='Telefone deve estar no formato (99) 99999-9999')])
    
    ativo = models.BooleanField(default=True)

    # Relacionamento
    equipe = models.ForeignKey(Equipe, on_delete=models.RESTRICT, related_name='membros', null=True, blank=True)

    def __str__(self):
        return f'{self.equipe} - {self.nome}' 

class Atividade(models.Model):
    nome = models.CharField(verbose_name='Nome da Atividade', max_length=100, blank=False, null=False)
    descricao =  models.CharField(verbose_name='Descrição', max_length=500, blank=False, null=False)
    dt_inicio = models.DateField(verbose_name='Data de início', blank=True, null=True)
    dt_limite =  models.DateField(verbose_name='Data Limite', blank=False, null=False)
    feito = models.BooleanField(default=False, blank=False, null=False)
    

    # Relacionamento
    projeto = models.ForeignKey('Projeto', on_delete=models.RESTRICT, related_name='atividades')
    membro = models.ForeignKey('Membro', on_delete=models.SET_NULL, related_name='atividades', null=True, blank=True)

    def clean(self):
      if self.dt_limite < self.dt_inicio:
        raise ValidationError('Data de fim deve ser após data de início ou igual')
      
    def clean_membro(self):
      if self.membro.equipe != self.projeto.equipe:
        raise ValidationError('Membro deve pertencer à equipe do projeto')


    def __str__(self):
        return f'{self.projeto} - {self.nome}'