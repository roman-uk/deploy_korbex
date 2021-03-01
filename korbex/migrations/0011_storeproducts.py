# Generated by Django 3.1.3 on 2020-12-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korbex', '0010_auto_20201224_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name_product', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
