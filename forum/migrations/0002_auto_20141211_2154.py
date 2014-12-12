# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
                ('categoria_pai', models.ForeignKey(blank=True, to='forum.Categoria', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='topico',
            name='categoria',
            field=models.ForeignKey(blank=True, to='forum.Categoria', null=True),
            preserve_default=True,
        ),
    ]
