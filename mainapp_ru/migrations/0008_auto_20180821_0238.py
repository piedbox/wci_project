# Generated by Django 2.0.7 on 2018-08-21 02:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_ru', '0007_auto_20180820_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeru',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='innerhomeru',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
