# Generated by Django 4.2.2 on 2023-07-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0033_londonfield_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='londonfield',
            old_name='age',
            new_name='age1',
        ),
        migrations.AddField(
            model_name='londonfield',
            name='age2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
