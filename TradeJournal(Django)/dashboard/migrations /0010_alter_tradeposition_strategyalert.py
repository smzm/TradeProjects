# Generated by Django 3.2.7 on 2021-10-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_rename_strategy_alert_tradeposition_strategyalert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradeposition',
            name='strategyAlert',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
