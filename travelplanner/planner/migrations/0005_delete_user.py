# Generated by Django 4.1.7 on 2023-06-11 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_remove_user_name_alter_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]