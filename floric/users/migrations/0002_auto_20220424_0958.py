# Generated by Django 3.2.7 on 2022-04-24 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bio',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='research',
        ),
        migrations.RemoveField(
            model_name='user',
            name='study',
        ),
        migrations.RemoveField(
            model_name='user',
            name='work',
        ),
    ]