# Generated by Django 2.0.7 on 2018-08-26 09:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_ru', '0008_auto_20180821_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientassesment',
            name='off_lang_en',
        ),
        migrations.RemoveField(
            model_name='clientassesment',
            name='off_lang_fr',
        ),
        migrations.RemoveField(
            model_name='homeru',
            name='body',
        ),
        migrations.AddField(
            model_name='clientassesment',
            name='off_lang_en_level',
            field=models.CharField(choices=[('0', 'Выбрать...'), ('1', 'Нет'), ('2', 'Начальный'), ('3', 'Средний'), ('4', 'Выше среднего'), ('5', 'Свободное')], default='0', max_length=15),
        ),
        migrations.AddField(
            model_name='clientassesment',
            name='off_lang_fr_level',
            field=models.CharField(choices=[('0', 'Выбрать...'), ('1', 'Нет'), ('2', 'Начальный'), ('3', 'Средний'), ('4', 'Выше среднего'), ('5', 'Свободное')], default='0', max_length=15),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='edu_level',
            field=models.CharField(choices=[('0', 'Выбрать...'), ('1', 'Школьное образование'), ('2', 'Незаконченное высшее'), ('3', 'Cреднее специальное'), ('4', 'Бакалавриат'), ('5', 'Магистратура'), ('6', 'Кандидат наук'), ('7', "Master's degree, or professional degree needed to practice in a licensed profession"), ('8', 'Doctoral level university degree (PhD)')], default='0', max_length=118),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='immigration_status',
            field=models.CharField(choices=[('0', 'Выбрать...'), ('1', 'Туристическая'), ('2', 'Студенческая'), ('3', 'Рабочая'), ('4', 'Нет')], default='0', error_messages={'invalid': 'Waehlen Sie die Zahlungsart!', 'required': 'Waehlen Sie die Zahlungsart!'}, max_length=14),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='marital_status',
            field=models.CharField(choices=[('0', 'Выбрать...'), ('1', 'Брак признанный недействительным'), ('2', 'В гражданском браке'), ('3', 'В разводе'), ('4', 'Не в браке'), ('5', 'В браке'), ('6', 'Вдовец / вдова')], default='0', max_length=22),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='partner_edu',
            field=models.CharField(choices=[('0', 'Выбрать...'), ('1', 'Школьное образование'), ('2', 'Незаконченное высшее'), ('3', 'Cреднее специальное'), ('4', 'Бакалавриат'), ('5', 'Магистратура'), ('6', 'Кандидат наук'), ('7', "Master's degree, or professional degree needed to practice in a licensed profession"), ('8', 'Doctoral level university degree (PhD)')], default='1', max_length=118),
        ),
        migrations.AlterField(
            model_name='homeru',
            name='paragraph1',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
