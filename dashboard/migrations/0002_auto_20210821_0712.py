# Generated by Django 3.2.6 on 2021-08-21 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradeposition',
            name='analysis',
        ),
        migrations.DeleteModel(
            name='Analysis',
        ),
        migrations.DeleteModel(
            name='ChartPatterns',
        ),
        migrations.DeleteModel(
            name='HarmonicPatterns',
        ),
        migrations.DeleteModel(
            name='TechnicalIndicators',
        ),
        migrations.DeleteModel(
            name='TradePosition',
        ),
        migrations.DeleteModel(
            name='TrendAnalysis',
        ),
        migrations.DeleteModel(
            name='WaveAnalysis',
        ),
    ]
