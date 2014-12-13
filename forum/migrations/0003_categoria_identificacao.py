# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20141211_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='identificacao',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
