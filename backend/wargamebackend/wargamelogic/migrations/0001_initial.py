# Generated by Django 5.1 on 2025-07-18 19:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bradley',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('classification', models.CharField(choices=[('BRADLEY', 'Bradley'), ('F18', 'F-18 Jet'), ('DESTROYER', 'Destroyer'), ('INFANTRY', 'Infantry Battalion')], max_length=50)),
                ('x_position', models.PositiveIntegerField()),
                ('y_position', models.PositiveIntegerField()),
                ('team', models.CharField(choices=[('RED', 'Red'), ('BLUE', 'Blue'), ('NEUTRAL', 'Neutral')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Destroyer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('classification', models.CharField(choices=[('BRADLEY', 'Bradley'), ('F18', 'F-18 Jet'), ('DESTROYER', 'Destroyer'), ('INFANTRY', 'Infantry Battalion')], max_length=50)),
                ('x_position', models.PositiveIntegerField()),
                ('y_position', models.PositiveIntegerField()),
                ('team', models.CharField(choices=[('RED', 'Red'), ('BLUE', 'Blue'), ('NEUTRAL', 'Neutral')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='F18',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('classification', models.CharField(choices=[('BRADLEY', 'Bradley'), ('F18', 'F-18 Jet'), ('DESTROYER', 'Destroyer'), ('INFANTRY', 'Infantry Battalion')], max_length=50)),
                ('x_position', models.PositiveIntegerField()),
                ('y_position', models.PositiveIntegerField()),
                ('team', models.CharField(choices=[('RED', 'Red'), ('BLUE', 'Blue'), ('NEUTRAL', 'Neutral')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
