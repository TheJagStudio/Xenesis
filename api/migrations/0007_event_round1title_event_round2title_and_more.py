# Generated by Django 4.1.4 on 2023-02-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_event_winnerprice1_event_winnerprice2"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="round1Title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="round2Title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="round3Title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="round4Title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="round5Title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
