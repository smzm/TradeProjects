# Generated by Django 3.2.6 on 2021-08-21 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_analysis_chartpatterns_harmonicpatterns_technicalindicators_tradeposition_trendanalysis_waveanalysis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysis',
            name='Chart_Patterns',
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='Harmonic_Patterns',
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='Technical_Indicators',
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='Trend_Analysis',
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='WaveAnalysis',
        ),
        migrations.DeleteModel(
            name='TradePosition',
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
            name='TrendAnalysis',
        ),
        migrations.DeleteModel(
            name='WaveAnalysis',
        ),
    ]
