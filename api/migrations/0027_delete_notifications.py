# Generated by Django 4.1.4 on 2024-02-01 11:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0026_delete_gallery"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Notifications",
        ),
    ]