# Generated by Django 4.2.1 on 2023-05-06 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TKTUsers', '0002_alter_ticketdetail_issue_related_to_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketdetail',
            name='ticket_assigned_to',
        ),
        migrations.RemoveField(
            model_name='ticketdetail',
            name='ticket_status',
        ),
        migrations.RemoveField(
            model_name='ticketdetail',
            name='website_technology',
        ),
    ]