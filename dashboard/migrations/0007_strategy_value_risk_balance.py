# Generated by Django 3.2.7 on 2021-10-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20211001_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='value_risk_balance',
            field=models.FloatField(null=True),
        ),
    ]
