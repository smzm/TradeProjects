# Generated by Django 3.2.7 on 2021-10-02 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_rename_remain_risk_strategy_new_position_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategy',
            name='equity',
        ),
    ]
