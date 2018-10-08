# Generated by Django 2.0.7 on 2018-08-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_ru', '0010_auto_20180826_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientassesment',
            name='edu_level',
            field=models.CharField(choices=[('0', 'Выбрать...'), ('1', 'Школьное образование'), ('2', 'Неоконченное высшее'), ('3', 'Cреднее специальное'), ('4', 'Бакалавриат'), ('5', 'Магистратура'), ('6', 'Кандидат наук')], default='0', max_length=118),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='partner_edu',
            field=models.CharField(choices=[('0', 'Выбрать...'), ('1', 'Школьное образование'), ('2', 'Неоконченное высшее'), ('3', 'Cреднее специальное'), ('4', 'Бакалавриат'), ('5', 'Магистратура'), ('6', 'Кандидат наук')], default='1', max_length=118),
        ),
    ]
