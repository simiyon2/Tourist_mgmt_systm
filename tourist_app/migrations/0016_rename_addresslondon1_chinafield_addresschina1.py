# Generated by Django 4.2.2 on 2023-07-19 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0015_rename_china_chinafield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chinafield',
            old_name='addresslondon1',
            new_name='addresschina1',
        ),
    ]