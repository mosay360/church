# Generated by Django 4.0.1 on 2022-03-16 11:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amchurch', '0002_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]