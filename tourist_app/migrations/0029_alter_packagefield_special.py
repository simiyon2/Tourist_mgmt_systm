# Generated by Django 4.2.2 on 2023-07-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0028_alter_packagefield_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagefield',
            name='special',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
