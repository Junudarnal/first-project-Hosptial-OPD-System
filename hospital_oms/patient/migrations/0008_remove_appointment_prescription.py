# Generated by Django 4.0.4 on 2022-06-03 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_appointment_prescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='Prescription',
        ),
    ]
