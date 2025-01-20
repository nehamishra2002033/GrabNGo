# Generated by Django 5.1.5 on 2025-01-18 18:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0007_remove_booktable_booking_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='booktable',
            old_name='Booking_date',
            new_name='booking_data',
        ),
        migrations.RemoveField(
            model_name='booktable',
            name='Name',
        ),
        migrations.AddField(
            model_name='booktable',
            name='user',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
