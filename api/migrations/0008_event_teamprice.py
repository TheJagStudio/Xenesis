# Generated by Django 4.1.4 on 2023-02-16 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_event_round1title_event_round2title_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="teamPrice",
            field=models.CharField(default="", max_length=10),
        ),
    ]
