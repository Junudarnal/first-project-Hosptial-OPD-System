# Generated by Django 4.0.4 on 2022-05-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_remove_appointment_doctorid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]