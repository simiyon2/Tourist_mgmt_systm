# Generated by Django 4.2.2 on 2023-07-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0045_payment_four'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_five',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentMethod', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('cardnumber', models.CharField(max_length=16, null=True)),
                ('expiration', models.CharField(max_length=20, null=True)),
                ('cvv', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='payment_six',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentMethod', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('cardnumber', models.CharField(max_length=16, null=True)),
                ('expiration', models.CharField(max_length=20, null=True)),
                ('cvv', models.CharField(max_length=3, null=True)),
            ],
        ),
    ]
