# Generated by Django 3.2.1 on 2021-06-08 14:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wconnects', '0006_dating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
