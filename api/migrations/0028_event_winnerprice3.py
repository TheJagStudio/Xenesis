# Generated by Django 4.1.4 on 2024-02-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0027_delete_notifications"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="winnerPrice3",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
