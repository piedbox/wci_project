# Generated by Django 2.0.7 on 2018-07-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_en', '0002_clientassesment'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientassesment',
            name='name',
            field=models.CharField(default=False, max_length=35),
        ),
    ]
