# Generated by Django 4.1.4 on 2024-02-01 11:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0029_remove_event_organisers_remove_event_volunteer_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="winner1",
        ),
        migrations.RemoveField(
            model_name="event",
            name="winner2",
        ),
        migrations.RemoveField(
            model_name="event",
            name="winner3",
        ),
    ]
