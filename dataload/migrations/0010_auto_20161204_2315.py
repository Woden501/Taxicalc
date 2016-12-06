# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataload', '0009_auto_20161204_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratecode',
            name='rateGroup',
            field=models.CharField(default='unknown', max_length=8),
        ),
        migrations.AddField(
            model_name='vendorinfo',
            name='vendorName',
            field=models.CharField(default='unknown', max_length=30),
        ),
        migrations.AlterField(
            model_name='fareinfo',
            name='paymentType',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='fareinfo',
            name='tripType',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='ratecode',
            name='rateType',
            field=models.CharField(max_length=21),
        ),
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
