# Generated by Django 4.0.4 on 2022-08-01 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_remove_doctor_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
    ]