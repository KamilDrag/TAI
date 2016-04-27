# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_auto_20160425_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 25, 21, 53, 17, 661514)),
        ),
    ]
