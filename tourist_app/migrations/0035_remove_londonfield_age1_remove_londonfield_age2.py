# Generated by Django 4.2.2 on 2023-07-23 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0034_rename_age_londonfield_age1_londonfield_age2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='londonfield',
            name='age1',
        ),
        migrations.RemoveField(
            model_name='londonfield',
            name='age2',
        ),
    ]
