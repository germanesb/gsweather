# Generated by Django 2.1 on 2020-07-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_remove_city_datetimetamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
