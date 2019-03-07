# Generated by Django 2.1.7 on 2019-03-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_respuestaoriginal_variable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestaaleatoria',
            name='orden',
        ),
        migrations.RemoveField(
            model_name='respuestaoriginal',
            name='orden',
        ),
        migrations.AddField(
            model_name='respuestaaleatoria',
            name='variable',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='pregunta_txt',
            field=models.CharField(max_length=400),
        ),
    ]
