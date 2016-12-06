from __future__ import unicode_literals

from django.db import models

import datetime


# Create your models here.
class TaxiLocation(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    borough = models.CharField(default='unknown', max_length=9)


class VendorInfo(models.Model):
    vendor_id = models.IntegerField()
    vendor_name = models.CharField(max_length=30, default='unknown')


class StoreAndForward(models.Model):
    store_and_fwd_flag = models.CharField(max_length=1)


class RateCode(models.Model):
    rate_code_id = models.IntegerField()
    rate_group = models.CharField(max_length=8, default='unknown')
    rate_type = models.CharField(max_length=21)


class FareInfo(models.Model):
    passenger_count = models.IntegerField(default=1)
    trip_distance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    trip_type = models.CharField(max_length=11)
    fare_amount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    extra = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    mta_tax = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    tip_amount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    tolls_amount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    ehail_fee = models.CharField(max_length=10)
    improvement_surcharge = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    total_amount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    payment_type = models.CharField(max_length=11)


class TaxiDatetime(models.Model):
    taxi_date = models.DateTimeField()
    year = models.IntegerField(default=2016)
    month = models.CharField(default='January', max_length=15)
    month_of_year = models.IntegerField(default=2016)
    week_of_year = models.IntegerField(default=0)
    day = models.CharField(default='Friday', max_length=15)
    day_of_week = models.IntegerField(default=0)
    day_of_month = models.IntegerField(default=0)
    day_of_year = models.IntegerField(default=0)
    hour = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)


class TaxiFare(models.Model):
    fare_pickup_location = models.ForeignKey(TaxiLocation, on_delete=models.CASCADE, related_name='pickupLocation', null=True)
    fare_dropoff_location = models.ForeignKey(TaxiLocation, on_delete=models.CASCADE, related_name='dropoffLocation', null=True)
    vendor_info = models.ForeignKey(VendorInfo, on_delete=models.CASCADE, null=True)
    store_and_forward_info = models.ForeignKey(StoreAndForward, on_delete=models.CASCADE, null=True)
    rate_code_info = models.ForeignKey(RateCode, on_delete=models.CASCADE, null=True)
    additional_fare_info = models.ForeignKey(FareInfo, on_delete=models.CASCADE, null=True)
    fare_pickup_time = models.ForeignKey(TaxiDatetime, on_delete=models.CASCADE, related_name='pickupTime', null=True)
    fare_dropoff_time = models.ForeignKey(TaxiDatetime, on_delete=models.CASCADE, related_name='dropoffTime', null=True)
