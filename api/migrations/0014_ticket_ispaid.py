# Generated by Django 4.1.4 on 2023-02-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_remove_profile_bio_remove_profile_birth_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="isPaid",
            field=models.BooleanField(default=False),
        ),
    ]