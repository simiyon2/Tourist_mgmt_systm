# Generated by Django 4.2.2 on 2023-07-30 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0048_alter_bookingfield_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingfield',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
