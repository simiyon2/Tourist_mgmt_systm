# Generated by Django 4.2.2 on 2023-07-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0013_alter_londonfield_addresslondon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='china',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addresschina', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('addresslondon1', models.CharField(max_length=100, null=True)),
                ('date1', models.DateField(null=True)),
                ('gender1', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
