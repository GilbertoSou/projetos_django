# Generated by Django 5.1.4 on 2025-01-22 19:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projeto', '0003_equipe_ativa_membro_genero_membro_telefone_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atividade',
            options={},
        ),
        migrations.AlterModelOptions(
            name='equipe',
            options={},
        ),
        migrations.AlterModelOptions(
            name='membro',
            options={},
        ),
        migrations.RemoveField(
            model_name='membro',
            name='funcao',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='orcamento',
        ),
        migrations.AddField(
            model_name='atividade',
            name='dt_inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Data de início'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='membro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atividades', to='app_projeto.membro'),
        ),
        migrations.AddField(
            model_name='membro',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='dt_limite',
            field=models.DateField(verbose_name='Data Limite'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='equipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='membros', to='app_projeto.equipe'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='telefone',
            field=models.CharField(help_text='(99) 99999-9999', max_length=15, validators=[django.core.validators.RegexValidator(message='Telefone deve estar no formato (99) 99999-9999', regex='^\\(\\d{2}\\) \\d{5}-\\d{4}$')]),
        ),
    ]
