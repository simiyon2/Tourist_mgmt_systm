# Generated by Django 4.2.2 on 2023-07-19 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0010_londonfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='londonfield',
            name='addresslondon',
            field=models.TextField(max_length=100, null=True),
        ),
    ]