# Generated by Django 4.1.3 on 2022-11-03 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_alter_gate_relay_open_barrier_pin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=50, unique=True)),
                ('entrance_datetime', models.DateTimeField(auto_now=True)),
                ('exit_datetime', models.DateTimeField(null=True)),
                ('entrance_gate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrance_gates', to='parking.gate')),
                ('exit_gate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exit_gates', to='parking.gate')),
            ],
        ),
    ]
