# Generated by Django 4.2.4 on 2023-09-08 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='name',
            new_name='task',
        ),
    ]