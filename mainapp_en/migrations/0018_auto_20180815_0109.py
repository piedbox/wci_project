# Generated by Django 2.0.7 on 2018-08-15 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_en', '0017_auto_20180731_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientassesment',
            name='nationality',
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='edu_level',
            field=models.CharField(choices=[('0', 'Please Choose...'), ('1', 'None, or less then secondary (high school)'), ('2', 'Secondary diploma (High school Diploma)'), ('3', 'One-year program at a university, college, trade or technical school, or other institute'), ('4', 'Two-year program at a university, college, trade or technical school, or other institute'), ('5', "Bachelor's degree (three or more year program at a university, college, trade or technical school, or other institute)"), ('6', 'Two or more certificates, diplomas, or degrees. One must be for a program of three or more years'), ('7', "Master's degree, or professional degree needed to practice in a licensed profession"), ('8', 'Doctoral level university degree (PhD)')], default='0', max_length=118),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='immigration_status',
            field=models.CharField(choices=[('0', 'Please Choose...'), ('1', 'Not Applicable'), ('2', 'Visitor'), ('3', 'Student'), ('4', 'Worker')], default='0', error_messages={'invalid': 'Waehlen Sie die Zahlungsart!', 'required': 'Waehlen Sie die Zahlungsart!'}, max_length=14),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='marital_status',
            field=models.CharField(choices=[('0', 'Please Choose...'), ('1', 'Annulled Marriage'), ('2', 'Common-Law'), ('3', 'Divorced / Separated'), ('4', 'Legally Separated'), ('5', 'Married'), ('6', 'Never Married / Single'), ('7', 'Widowed')], default='0', max_length=22),
        ),
        migrations.AlterField(
            model_name='clientassesment',
            name='partner_edu',
            field=models.CharField(blank=True, choices=[('0', 'Please Choose...'), ('1', 'None, or less then secondary (high school)'), ('2', 'Secondary diploma (High school Diploma)'), ('3', 'One-year program at a university, college, trade or technical school, or other institute'), ('4', 'Two-year program at a university, college, trade or technical school, or other institute'), ('5', "Bachelor's degree (three or more year program at a university, college, trade or technical school, or other institute)"), ('6', 'Two or more certificates, diplomas, or degrees. One must be for a program of three or more years'), ('7', "Master's degree, or professional degree needed to practice in a licensed profession"), ('8', 'Doctoral level university degree (PhD)')], default='0', max_length=118),
        ),
    ]