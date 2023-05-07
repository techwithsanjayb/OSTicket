# Generated by Django 4.2.1 on 2023-05-06 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TKTUsers', '0008_ticketdetail_website_technology'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketdetail',
            name='website_technology',
        ),
        migrations.AddField(
            model_name='ticketdetail',
            name='website_technology',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TKTUsers.technology_stack'),
        ),
    ]