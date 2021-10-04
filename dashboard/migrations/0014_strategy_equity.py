# Generated by Django 3.2.7 on 2021-10-01 19:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_remainrisk_strategy'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='equity',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]