# Generated by Django 4.1.3 on 2023-03-01 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_ticket_acceptedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='acceptedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name_acceptedBy', to='api.profile'),
        ),
    ]
