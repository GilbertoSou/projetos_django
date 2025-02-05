from django.contrib import admin
from app_projeto.models import Projeto, Equipe, Membro, Atividade


class AtividadeInline(admin.TabularInline):
    model = Atividade
    fields = ('nome', 'membro', 'horas_estimadas', 'data_inicio')
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
      if db_field.name == "membro":
        if request.resolver_match:
          projeto_id = request.resolver_match.kwargs.get('projeto_id')
          if projeto_id:
            kwargs["queryset"] = Membro.objects.filter(equipe__projeto__id=projeto_id)
      return super().formfield_for_foreignkey(db_field, request, **kwargs)

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

    inlines = [AtividadeInline]


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativa', 'count_membros')
    list_filter = ('ativa',)

    inlines = [MembroInline]


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'nome', 'membro', 'dt_limite', 'feito',)
    list_filter = ('projeto', 'membro',)