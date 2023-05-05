# Generated by Django 4.2.1 on 2023-05-05 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TKTUsers', '0002_agent_role_agent_role_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_status_choice',
            name='Ticket_status_created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket_status_choice',
            name='Ticket_status_update_date',
            field=models.DateField(auto_now=True),
        ),
    ]
