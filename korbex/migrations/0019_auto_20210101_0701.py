# Generated by Django 3.1.3 on 2021-01-01 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('korbex', '0018_auto_20210101_0637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdata',
            old_name='addres',
            new_name='address',
        ),
    ]
