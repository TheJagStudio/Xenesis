# Generated by Django 4.1.4 on 2023-02-22 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_alter_ticket_paymentmethod"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="owner1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner1_ticket",
                to="api.profile",
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="owner2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner2_ticket",
                to="api.profile",
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="owner3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner3_ticket",
                to="api.profile",
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="owner4",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner4_ticket",
                to="api.profile",
            ),
        ),
    ]