# Generated by Django 3.2.7 on 2021-10-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='linkedin_account',
        ),
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
