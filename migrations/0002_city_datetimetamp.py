# Generated by Django 2.1 on 2020-06-29 23:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='datetimetamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 19, 18, 23, 618346)),
        ),
    ]
