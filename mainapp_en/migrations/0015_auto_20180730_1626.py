# Generated by Django 2.0.7 on 2018-07-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_en', '0014_auto_20180730_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientassesment',
            name='canadian_cert',
            field=models.CharField(choices=[(True, 'Yes'), (False, 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='canadian_dipl',
            field=models.CharField(choices=[(True, 'Yes'), (False, 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='nomin_cert',
            field=models.CharField(choices=[(True, 'Yes'), (False, 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='partner_status_of_canada',
            field=models.CharField(choices=[(True, 'Yes'), (False, 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='partner_track',
            field=models.CharField(choices=[(True, 'Yes'), (False, 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='sibling_in_canada',
            field=models.CharField(choices=[(True, 'Yes'), (False, 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='valid_job',
            field=models.CharField(choices=[(True, 'Yes'), (False, 'No')], max_length=3),
        ),
    ]
