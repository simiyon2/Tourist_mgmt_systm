# Generated by Django 4.2.2 on 2023-07-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourist',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
    ]