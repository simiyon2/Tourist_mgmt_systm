# Generated by Django 4.2.2 on 2023-07-28 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0038_rename_date_londonfield_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='londonfield',
            old_name='addresslondon',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='londonfield',
            old_name='addresslondon1',
            new_name='name1',
        ),
    ]
