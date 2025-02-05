from django.contrib import admin
from app_projeto.models import Projeto, Equipe, Membro, Atividade


class MembroInline(admin.TabularInline):
    model =  Membro
    extra = 0
    fields = ('nome', 'genero')


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'equipe', 'dt_inicio', 'dt_final')
    search_fields = ('nome', 'descricao', )
    list_filter = ('equipe',)
    date_hierarchy = 'dt_inicio'


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativa', 'count_membros')
    list_filter = ('ativa',)

    inlines = [MembroInline]


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'nome', 'membro', 'dt_limite', 'feito',)
    list_filter = ('projeto', 'membro',)