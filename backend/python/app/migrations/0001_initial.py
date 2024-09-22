# Generated by Django 5.1.1 on 2024-09-22 01:14

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('unit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.unit')),
            ],
            options={
                'abstract': False,
            },
            bases=('app.unit',),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('unit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.unit')),
            ],
            options={
                'abstract': False,
            },
            bases=('app.unit',),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.unit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
