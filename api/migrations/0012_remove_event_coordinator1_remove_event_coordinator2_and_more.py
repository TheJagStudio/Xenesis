# Generated by Django 4.1.4 on 2023-02-21 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_department_abbriviation"),
    ]

    operations = [
        migrations.RemoveField(model_name="event", name="coordinator1",),
        migrations.RemoveField(model_name="event", name="coordinator2",),
        migrations.AddField(
            model_name="event",
            name="organiser1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organiser1_event",
                to="api.profile",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="organiser2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organiser2_event",
                to="api.profile",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="organiser3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organiser3_event",
                to="api.profile",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="organiser4",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organiser4_event",
                to="api.profile",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="organiser5",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organiser5_event",
                to="api.profile",
            ),
        ),
    ]
