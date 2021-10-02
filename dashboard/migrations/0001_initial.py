# Generated by Django 3.2.7 on 2021-10-01 11:32

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChartPatterns',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FundamentalAnalysis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HarmonicPatterns',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('body', models.TextField(max_length=1000)),
                ('is_read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('emotion', models.CharField(choices=[('fear', 'Fear'), ('hope', 'Hope'), ('stress', 'Stress'), ('calm', 'Calm'), ('happy', 'Happy'), ('sad', 'Sad')], max_length=10)),
                ('body', models.TextField(max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('balance', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('risk_on_balance', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('value_risk', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalIndicators',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TradePosition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('symbol', models.CharField(max_length=200)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('size', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('side', models.CharField(choices=[('Long', 'Long'), ('Short', 'Short')], max_length=6)),
                ('takeprofit', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('stoploss', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TrendAnalysis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaveAnalysis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
