# Generated by Django 4.0.4 on 2022-05-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctor_contact_no_doctor_full_name_doctor_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='doctor',
            name='username',
            field=models.CharField(default='doctor_abc', max_length=20),
        ),
    ]
