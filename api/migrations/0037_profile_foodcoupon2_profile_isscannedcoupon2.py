# Generated by Django 4.1.4 on 2024-02-22 01:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0036_event_maxticket"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="foodCoupon2",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name="profile",
            name="isScannedCoupon2",
            field=models.BooleanField(default=False),
        ),
    ]