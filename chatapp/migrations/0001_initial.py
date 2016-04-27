# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nick', models.CharField(max_length=20)),
                ('message_date', models.DateField(default=datetime.datetime(2016, 4, 25, 21, 43, 3, 740564))),
                ('message_content', models.CharField(max_length=80)),
            ],
        ),
    ]
