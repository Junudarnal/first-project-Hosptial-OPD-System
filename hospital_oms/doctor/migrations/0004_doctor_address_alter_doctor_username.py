# Generated by Django 4.0.4 on 2022-06-01 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_doctor_email_doctor_password_doctor_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
