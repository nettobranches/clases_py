# Generated by Django 2.1.7 on 2019-03-29 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0012_auto_20190329_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestaaleatoria',
            name='res',
            field=models.CharField(max_length=100),
        ),
    ]
