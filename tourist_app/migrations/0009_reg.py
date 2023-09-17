# Generated by Django 4.2.2 on 2023-07-11 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0008_delete_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('file', models.FileField(null=True, upload_to='image/')),
                ('email', models.EmailField(max_length=30, null=True)),
                ('phonenumber', models.IntegerField(null=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('confirmpassword', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
