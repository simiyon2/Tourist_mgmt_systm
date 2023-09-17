# Generated by Django 4.2.2 on 2023-07-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0021_malaysiafield'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('subject', models.CharField(max_length=50, null=True)),
                ('message', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
