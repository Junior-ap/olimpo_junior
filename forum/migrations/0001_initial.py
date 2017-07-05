# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 12:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(default=False, verbose_name='Correta?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Resposta',
                'ordering': ['-correct', 'created'],
                'verbose_name_plural': 'Respostas',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('body', models.TextField(verbose_name='Menssagem')),
                ('views', models.IntegerField(blank=True, default=0, verbose_name='Visualizações')),
                ('answers', models.IntegerField(blank=True, default=0, verbose_name='Respostas')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Tópico',
                'ordering': ['-updated'],
                'verbose_name_plural': 'Tópicos',
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='forum.Topic', verbose_name='Tópico'),
        ),
    ]