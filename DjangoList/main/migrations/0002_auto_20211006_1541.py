# Generated by Django 3.2.7 on 2021-10-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Список'},
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(max_length=50, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
    ]
