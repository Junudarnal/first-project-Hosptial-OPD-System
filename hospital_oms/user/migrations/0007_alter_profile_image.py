# Generated by Django 4.0.4 on 2022-08-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='doctor.jpg', upload_to='profile/'),
        ),
    ]