# Generated by Django 3.1.3 on 2020-11-17 19:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
