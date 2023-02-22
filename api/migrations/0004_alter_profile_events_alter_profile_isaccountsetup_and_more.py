# Generated by Django 4.1.4 on 2023-02-14 00:33

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_profile_isverified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="events",
            field=models.JSONField(default=api.models.Profile.default_data),
        ),
        migrations.AlterField(
            model_name="profile",
            name="isAccountSetup",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="profile",
            name="isOrganiser",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="profile",
            name="isVolunteer",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="profile",
            name="notification",
            field=models.JSONField(default=api.models.Profile.default_data),
        ),
        migrations.AlterField(
            model_name="profile",
            name="profilePic",
            field=models.CharField(default="0001", max_length=100),
        ),
    ]