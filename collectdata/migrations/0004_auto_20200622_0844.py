# Generated by Django 3.0.2 on 2020-06-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectdata', '0003_auto_20200622_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacollection',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='stop_time',
            field=models.TimeField(null=True),
        ),
    ]