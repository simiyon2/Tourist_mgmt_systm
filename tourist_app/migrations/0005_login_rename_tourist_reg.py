# Generated by Django 4.2.2 on 2023-07-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0004_delete_reg_tourist_confirmpassword_tourist_email_and_more'),
    ]

    operations = [
        migrations.CreateModel( 
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='tourist',
            new_name='reg',
        ),
    ]
