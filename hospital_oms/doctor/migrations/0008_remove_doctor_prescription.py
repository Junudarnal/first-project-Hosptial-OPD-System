# Generated by Django 4.0.4 on 2022-06-03 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_doctor_prescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='Prescription',
        ),
    ]
