# Generated by Django 4.0.4 on 2022-06-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_alter_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Prescription',
            field=models.ImageField(default='abc.png', upload_to='prescription'),
        ),
    ]
