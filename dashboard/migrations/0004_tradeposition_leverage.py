# Generated by Django 3.2.7 on 2021-10-01 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20211001_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradeposition',
            name='leverage',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]