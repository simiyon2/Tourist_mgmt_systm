# Generated by Django 4.2.2 on 2023-07-08 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0005_login_rename_tourist_reg'),
    ]

    operations = [
        migrations.DeleteModel(
            name='reg',
        ),
    ]
