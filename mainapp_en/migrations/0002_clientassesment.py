# Generated by Django 2.0.7 on 2018-07-27 13:03

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_en', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAssesment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_doc_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('marital_status', models.CharField(max_length=20)),
                ('nationality', models.CharField(blank=True, max_length=25)),
                ('dob', models.DateField()),
                ('immigration_status', models.CharField(choices=[('1', 'Not Applicable'), ('2', 'Visitor'), ('3', 'Student'), ('4', 'Worker')], max_length=125)),
                ('edu_level', models.CharField(choices=[('1', 'None, or less then secondary (high school)'), ('2', 'Secondary diploma (High school Diploma)'), ('3', 'One-year program at a university, college, trade or technical school, or other institute'), ('4', 'Two-year program at a university, college, trade or technical school, or other institute'), ('5', "Bachelor's degree (three or more year program at a university, college, trade or technical school, or other institute)"), ('6', 'Two or more certificates, diplomas, or degrees. One must be for a program of three or more years'), ('7', "Master's degree, or professional degree needed to practice in a licensed profession"), ('8', 'Doctoral level university degree (PhD)')], max_length=125)),
                ('canadian_dipl', models.BooleanField()),
                ('school_progr_name', models.TextField()),
                ('off_lang_en', models.CharField(max_length=40)),
                ('off_lang_fr', models.CharField(max_length=40)),
                ('work_exp_canada', models.TextField()),
                ('work_exp_home', models.TextField()),
                ('canadian_cert', models.BooleanField()),
                ('valid_job', models.BooleanField()),
                ('nomin_cert', models.BooleanField()),
                ('partner_status_of_canada', models.BooleanField()),
                ('partner_track', models.BooleanField()),
                ('partner_edu', models.CharField(choices=[('1', 'None, or less then secondary (high school)'), ('2', 'Secondary diploma (High school Diploma)'), ('3', 'One-year program at a university, college, trade or technical school, or other institute'), ('4', 'Two-year program at a university, college, trade or technical school, or other institute'), ('5', "Bachelor's degree (three or more year program at a university, college, trade or technical school, or other institute)"), ('6', 'Two or more certificates, diplomas, or degrees. One must be for a program of three or more years'), ('7', "Master's degree, or professional degree needed to practice in a licensed profession"), ('8', 'Doctoral level university degree (PhD)')], max_length=125)),
                ('partner_work_exp', models.TextField()),
                ('partner_lang', models.CharField(max_length=40)),
                ('sibling_in_canada', models.BooleanField()),
                ('memo', models.TextField()),
            ],
        ),
    ]
