# Generated by Django 2.2.1 on 2019-05-16 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestaoriginal',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
