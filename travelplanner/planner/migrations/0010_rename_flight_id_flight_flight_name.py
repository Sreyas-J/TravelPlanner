# Generated by Django 4.1.7 on 2023-06-13 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0009_flight_flight_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='flight_id',
            new_name='flight_name',
        ),
    ]