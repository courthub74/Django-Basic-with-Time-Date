# Generated by Django 3.0.5 on 2020-05-06 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200506_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='away',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='time',
            name='home',
        ),
    ]