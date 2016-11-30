from __future__ import unicode_literals

from django.db import models

import datetime


# Create your models here.
class TaxiLocation(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    borough = models.CharField(default='unknown', max_length=9)


class VendorInfo(models.Model):
    vendorId = models.IntegerField()


class StoreAndForward(models.Model):
    storeAndFwdFlag = models.CharField(max_length=1)


class RateCode(models.Model):
    rateCodeId = models.IntegerField()
    rateType = models.CharField(max_length=8)


class FareInfo(models.Model):
    passengerCount = models.IntegerField(default=1)
    tripDistance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    tripType = models.IntegerField(default=1, null=False, blank=False)
    fareAmount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    extra = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    mtaTax = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    tipAmount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    tollsAmount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    ehailFee = models.CharField(max_length=10)
    improvementSurcharge = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    totalAmount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    paymentType = models.IntegerField(default=3)


class TaxiDatetime(models.Model):
    taxiDate = models.DateTimeField()
    year = models.IntegerField(default=2016)
    month = models.CharField(default='January', max_length=15)
    monthOfYear = models.IntegerField(default=2016)
    weekOfYear = models.IntegerField(default=0)
    day = models.CharField(default='Friday', max_length=15)
    dayOfWeek = models.IntegerField(default=0)
    dayOfMonth = models.IntegerField(default=0)
    dayOfYear = models.IntegerField(default=0)
    hour = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)


class TaxiFare(models.Model):
    farePickupLocation = models.ForeignKey(TaxiLocation, on_delete=models.CASCADE, related_name='pickupLocation', null=True)
    fareDropoffLocation = models.ForeignKey(TaxiLocation, on_delete=models.CASCADE, related_name='dropoffLocation', null=True)
    vendorInfo = models.ForeignKey(VendorInfo, on_delete=models.CASCADE, null=True)
    storeAndForwardInfo = models.ForeignKey(StoreAndForward, on_delete=models.CASCADE, null=True)
    rateCodeInfo = models.ForeignKey(RateCode, on_delete=models.CASCADE, null=True)
    additionalFareInfo = models.ForeignKey(FareInfo, on_delete=models.CASCADE, null=True)
    farePickupTime = models.ForeignKey(TaxiDatetime, on_delete=models.CASCADE, related_name='pickupTime', null=True)
    fareDropoffTime = models.ForeignKey(TaxiDatetime, on_delete=models.CASCADE, related_name='dropoffTime', null=True)
