# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('votos', models.IntegerField(default=0, blank=True)),
                ('conteudo', models.CharField(max_length=2000)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('votos', models.IntegerField(default=0, blank=True)),
                ('conteudo', models.CharField(max_length=2000)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200, blank=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('labels', models.ManyToManyField(to='forum.Label', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsuarioForum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topicos_acompanhados', models.ManyToManyField(to='forum.Topico', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='topico',
            field=models.ForeignKey(to='forum.Topico'),
            preserve_default=True,
        ),
    ]
