# Generated by Django 4.0.4 on 2022-05-25 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0002_rename_appointmentdate_appointment_appointment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctorId',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient_id',
        ),
        migrations.AddField(
            model_name='appointment',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists')], default='Cardiologist', max_length=40),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointment', to='doctor.doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
    ]
