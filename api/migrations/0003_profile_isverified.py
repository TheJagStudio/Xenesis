# Generated by Django 4.1.4 on 2023-02-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_profile_college"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="isVerified",
            field=models.BooleanField(default=False),
        ),
    ]
