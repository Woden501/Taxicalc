from django.http import HttpResponse

import csv, loadHelper

import models

# Create your views here.
def index(request):
    return HttpResponse("This is the index page")

def load(request):
    # with open('green_tripdata_2016-06.csv') as f:
    with open('shortDataset.csv') as f:
        reader = csv.reader(f, delimiter=b",")
        header = next(reader)
        for row in reader:
            if not loadHelper.has_nulls(row):
                pickup_location = models.TaxiLocation.objects.create(longitude=row[5], latitude=row[6],
                                                                     borough=loadHelper.get_borough(longitude=row[5],
                                                                                                    latitude=row[6]))
                dropoff_location = models.TaxiLocation.objects.create(longitude=row[7], latitude=row[8],
                                                                      borough=loadHelper.get_borough(longitude=row[7],
                                                                                                     latitude=row[8]))
                vendor_info =  models.VendorInfo.objects.get_or_create(vendorId=row[0])[0]
                store_and_forward_info = models.StoreAndForward.objects.get_or_create(storeAndFwdFlag=row[3])[0]
                rate_code_info = models.RateCode.objects.get_or_create(rateCodeId=row[4],
                                                                rateType=loadHelper.find_rate_type(row[4]))[0]
                fare_info = models.FareInfo.objects.create(passengerCount=row[9], tripDistance=row[10],
                                                           tripType=row[20], fareAmount=row[11], extra=row[12],
                                                           mtaTax=row[13], tipAmount=row[14], tollsAmount=row[15],
                                                           ehailFee=row[16], improvementSurcharge=row[17],
                                                           totalAmount=row[18], paymentType=row[19])
                time_data = loadHelper.get_time_data(row[1])
                pickup_time = models.TaxiDatetime.objects.create(taxiDate=row[1], year=time_data.get('year'),
                                                                 month=time_data.get('month'),
                                                                 monthOfYear=time_data.get('month_of_year'),
                                                                 weekOfYear=time_data.get('week_of_year'),
                                                                 day=time_data.get('day'),
                                                                 dayOfWeek=time_data.get('day_of_week'),
                                                                 dayOfMonth=time_data.get('day_of_month'),
                                                                 dayOfYear=time_data.get('day_of_year'),
                                                                 hour=time_data.get('hour'),
                                                                 minute=time_data.get('minute'),
                                                                 second=time_data.get('second'))
                time_data = loadHelper.get_time_data(row[2])
                dropoff_time = models.TaxiDatetime.objects.create(taxiDate=row[2], year=time_data.get('year'),
                                                                 month=time_data.get('month'),
                                                                 monthOfYear=time_data.get('month_of_year'),
                                                                 weekOfYear=time_data.get('week_of_year'),
                                                                 day=time_data.get('day'),
                                                                 dayOfWeek=time_data.get('day_of_week'),
                                                                 dayOfMonth=time_data.get('day_of_month'),
                                                                 dayOfYear=time_data.get('day_of_year'),
                                                                 hour=time_data.get('hour'),
                                                                 minute=time_data.get('minute'),
                                                                 second=time_data.get('second'))
                models.TaxiFare.objects.create(farePickupLocation=pickup_location,
                                               fareDropoffLocation=dropoff_location,
                                               vendorInfo=vendor_info,
                                               storeAndForwardInfo=store_and_forward_info,
                                               rateCodeInfo=rate_code_info,
                                               additionalFareInfo=fare_info,
                                               farePickupTime=pickup_time,
                                               fareDropoffTime=dropoff_time,)
    return HttpResponse("The data load has completed")
