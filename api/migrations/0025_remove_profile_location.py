# Generated by Django 4.1.4 on 2024-02-01 11:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0024_event_organiser6"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="location",
        ),
    ]