# Generated by Django 3.2.7 on 2021-09-09 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_delete_messages'),
        ('dashboard', '0016_messages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
    ]
