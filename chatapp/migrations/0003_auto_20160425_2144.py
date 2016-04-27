# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_auto_20160425_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 25, 19, 44, 15, 385564, tzinfo=utc)),
        ),
    ]
