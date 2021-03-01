# Generated by Django 3.1.3 on 2021-02-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korbex', '0023_auto_20210130_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=20, verbose_name='Awtor artyklu'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='Treść'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_image', verbose_name='Obrazek do artyklu'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Tytulł'),
        ),
    ]