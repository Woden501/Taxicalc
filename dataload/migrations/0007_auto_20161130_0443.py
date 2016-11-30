# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataload', '0006_auto_20161130_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxifare',
            name='fareDropoffTime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dropoffTime', to='dataload.TaxiDatetime'),
        ),
        migrations.AlterField(
            model_name='taxifare',
            name='farePickupTime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pickupTime', to='dataload.TaxiDatetime'),
        ),
    ]
