# Generated by Django 4.0 on 2021-12-16 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='countdown',
            new_name='due',
        ),
    ]
