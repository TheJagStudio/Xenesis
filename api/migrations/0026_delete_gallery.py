# Generated by Django 4.1.4 on 2024-02-01 11:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0025_remove_profile_location"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Gallery",
        ),
    ]
