# Generated by Django 2.0.7 on 2018-08-27 02:04

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_en', '0025_auto_20180826_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_doc_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=30)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('citizenship', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=45)),
                ('dob', models.DateField()),
                ('marital_status', models.CharField(choices=[('0', 'Please Choose...'), ('1', 'Married'), ('2', 'Common-Law'), ('3', 'Single / Divorced')], default='0', max_length=22)),
                ('edu_level', models.CharField(choices=[('0', 'Please Choose...'), ('1', 'None, or less then secondary (high school)'), ('2', 'Secondary diploma (High school Diploma)'), ('3', 'College certificate'), ('4', "Bachelor's degree"), ('5', "Master's degree"), ('6', 'Doctoral university degree (PhD)')], default='0', max_length=118)),
                ('off_lang_en_level', models.CharField(choices=[('0', 'Please Choose...'), ('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Advanced'), ('4', 'Fluent')], default='0', max_length=15)),
                ('off_lang_fr_level', models.CharField(choices=[('0', 'Please Choose...'), ('1', 'Not applicable'), ('2', 'Beginner'), ('3', 'Intermediate'), ('4', 'Advanced'), ('5', 'Fluent')], default='0', max_length=15)),
                ('en_fr_cert', models.TextField(blank=True)),
                ('int_program', models.CharField(choices=[('0', 'Please Choose...'), ('1', 'English language courses'), ('2', 'French language courses'), ('3', 'Kids and teens camp programs'), ('4', 'College or university preparation'), ('5', 'University'), ('5', 'Postsecondary diploma'), ('5', 'Masters degree'), ('5', 'PhD')], default='0', max_length=15)),
                ('plan_date', models.DateField()),
                ('pref_province', models.CharField(blank=True, max_length=40)),
                ('plan_budget', models.CharField(max_length=15)),
                ('visa_rejected', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=3)),
                ('memo', models.TextField(blank=True)),
            ],
        ),
    ]