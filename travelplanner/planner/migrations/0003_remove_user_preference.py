# Generated by Django 4.1.7 on 2023-06-10 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_user_location_user_name_user_preference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Preference',
        ),
    ]
