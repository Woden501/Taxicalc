from __future__ import unicode_literals

from django.db import models


# Create your models here.
class TaxiFare(models.Model):
    vendorId = models.IntegerField()
    lpepPickupDatetime = models.DateTimeField()
    lpepDropoffDatetime = models.DateTimeField()
    storeAndFwdFlag = models.CharField(max_length=1)
    rateCodeId = models.IntegerField()
    pickupLongitude = models.DecimalField(max_digits=9, decimal_places=6)
    pickupLatitude = models.DecimalField(max_digits=9, decimal_places=6)
    dropoffLongitude = models.DecimalField(max_digits=9, decimal_places=6)
    dropoffLatitude = models.DecimalField(max_digits=9, decimal_places=6)
    passengerCount = models.IntegerField()
    tripDistance = models.DecimalField(max_digits=9, decimal_places=2)
    fareAmount = models.DecimalField(max_digits=9, decimal_places=2)
    extra = models.DecimalField(max_digits=9, decimal_places=2)
    mtaTax = models.DecimalField(max_digits=9, decimal_places=2)
    tipAmount = models.DecimalField(max_digits=9, decimal_places=2)
    tollsAmount = models.DecimalField(max_digits=9, decimal_places=2)
    ehailFee = models.CharField(max_length=10)
    improvementSurcharge = models.DecimalField(max_digits=9, decimal_places=2)
    totalAmount = models.DecimalField(max_digits=9, decimal_places=2)
    paymentType = models.IntegerField()
    tripType = models.IntegerField()