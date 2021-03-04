# Generated by Django 3.1.7 on 2021-03-04 20:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('korbex', '0026_auto_20210218_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Obrazek do artyklu'),
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='storeproducts',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Obrazek do towaru'),
        ),
    ]