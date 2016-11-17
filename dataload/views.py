from django.http import HttpResponse

import csv

from models import TaxiFare

# Create your views here.
def index(request):
    return HttpResponse("This is the index page")

def load(request):
    with open('green_tripdata_2016-06.csv') as f:
        reader = csv.reader(f, delimiter=b",")
        header = next(reader)
        TaxiFare.objects.bulk_create([TaxiFare(vendorId=row[0], lpepPickupDatetime=row[1],
                                               lpepDropoffDatetime=row[2], storeAndFwdFlag=row[3],
                                               rateCodeId=row[4], pickupLongitude=row[5],
                                               pickupLatitude=row[6], dropoffLongitude=row[7],
                                               dropoffLatitude=row[8], passengerCount=row[9],
                                               tripDistance=row[10], fareAmount=row[11],
                                               extra=row[12], mtaTax=row[13], tipAmount=row[14],
                                               tollsAmount=row[15], ehailFee=row[16],
                                               improvementSurcharge=row[17], totalAmount=row[18],
                                               paymentType=row[19], tripType=row[20],) for row in reader])
    return HttpResponse("The data load has completed")