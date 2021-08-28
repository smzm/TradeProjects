# Generated by Django 3.2.6 on 2021-08-21 15:12

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0006_auto_20210821_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartPatterns',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(choices=[('Double_Top_or_Bottom', 'Double Top or Bottom'), ('Head_and_Shoulders', 'Head and Shoulders'), ('Cup_and_Handle', 'Cup and Handle'), ('Flag', 'Flag'), ('Rectangle', 'Rectangle'), ('Parallel_Channel', 'Parallel Channel'), ('Pitchforks', 'Pitchforks'), ('Triangle', 'Triangle'), ('Gan', 'Gan')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HarmonicPatterns',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(choices=[('ABCD', 'ABCD'), ('Three_Drives', 'Three Drives'), ('Gartley', 'Gartley'), ('Bat', 'Bat'), ('Butterfly', 'Butterfly'), ('Crab', 'Crab'), ('Cypher', 'Cypher'), ('Five_Zero', 'Five_Zero'), ('Shark', 'Shark')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalIndicators',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(choices=[('Oscilators', 'Oscilators'), ('Volatility', 'Volatility'), ('Volume', 'Volume'), ('Moving_Average', 'Moving Average'), ('Bill_Wiliams', 'Bill Wiliams')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TradePosition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('symbol', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('side', models.CharField(choices=[('Long', 'Long'), ('Short', 'Short')], max_length=200)),
                ('size', models.FloatField()),
                ('levarage', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)])),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TrendAnalysis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(choices=[('Support_And_Resistance', 'Support And Resistance'), ('Supply_and_Demand', 'Supply and Demand'), ('Pivot_Points', 'Pivot Points'), ('Fibonacci', 'Fibonacci'), ('Trend_Lines', 'Trend Lines'), ('Candlestick_Analysis', 'Candlestick Analysis'), ('Multiple_Time_Frame_Analysis', 'Multiple Time Frame Analysis'), ('Fractals', 'Fractals'), ('Cycles', 'Cycles')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WaveAnalysis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(choices=[('Neo_Wave', 'Neo Wave'), ('Sine_Wave', 'Sine Wave'), ('Wolfe_Wave', 'Wolfe Wave')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Chart_Patterns', models.ManyToManyField(blank=True, to='dashboard.ChartPatterns')),
                ('Harmonic_Patterns', models.ManyToManyField(blank=True, to='dashboard.HarmonicPatterns')),
                ('Technical_Indicators', models.ManyToManyField(blank=True, to='dashboard.TechnicalIndicators')),
                ('Trend_Analysis', models.ManyToManyField(blank=True, to='dashboard.TrendAnalysis')),
                ('WaveAnalysis', models.ManyToManyField(blank=True, to='dashboard.WaveAnalysis')),
            ],
        ),
    ]
