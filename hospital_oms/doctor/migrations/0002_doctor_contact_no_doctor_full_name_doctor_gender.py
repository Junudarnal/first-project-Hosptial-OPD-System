# Generated by Django 4.0.4 on 2022-05-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='contact_no',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doctor',
            name='full_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(default='', max_length=6),
        ),
    ]