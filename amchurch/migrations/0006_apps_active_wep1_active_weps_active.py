# Generated by Django 4.0.1 on 2022-03-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amchurch', '0005_apps_desc_wep1_desc_weps_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='wep1',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='weps',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
