# Generated by Django 3.2.7 on 2021-10-01 12:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_tradeposition_leverage'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='risk_position',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]