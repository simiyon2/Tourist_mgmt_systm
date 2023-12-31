# Generated by Django 4.2.2 on 2023-07-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0003_reg'),
    ]

    operations = [
        migrations.DeleteModel(
            name='reg',
        ),
        migrations.AddField(
            model_name='tourist',
            name='confirmpassword',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tourist',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tourist',
            name='file',
            field=models.FileField(null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tourist',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
