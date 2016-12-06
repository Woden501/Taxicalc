from django.http import HttpResponse, Http404
from django.shortcuts import render

import csv, loadHelper

import models


# Create your views here.
def load(request):
    # with open('green_tripdata_2016-06.csv') as f:
    with open('every100thSample.csv') as f:
        reader = csv.reader(f, delimiter=b",")
        header = next(reader)
        for row in reader:
            if loadHelper.is_valid(row):
                pickup_location = models.TaxiLocation.objects.create(longitude=row[5], latitude=row[6],
                                                                     borough=loadHelper.get_borough(longitude=row[5],
                                                                                                    latitude=row[6]))
                dropoff_location = models.TaxiLocation.objects.create(longitude=row[7], latitude=row[8],
                                                                      borough=loadHelper.get_borough(longitude=row[7],
                                                                                                     latitude=row[8]))
                vendor_info =  models.VendorInfo.objects.get_or_create(vendor_id=row[0], vendor_name=loadHelper.get_vendor_name(row[0]))[0]
                store_and_forward_info = models.StoreAndForward.objects.get_or_create(store_and_fwd_flag=row[3])[0]
                rate_info = loadHelper.find_rate_info(row[4])
                rate_code_info = models.RateCode.objects.get_or_create(rate_code_id=row[4],
                                                                       rate_group=rate_info.get('group'),
                                                                       rate_type=rate_info.get('type'))[0]
                fare_data = loadHelper.get_fare_data(row[20], row[19])
                fare_info = models.FareInfo.objects.create(passenger_count=row[9], trip_distance=row[10],
                                                           trip_type=fare_data.get('trip_type'), fare_amount=row[11],
                                                           extra=row[12], mta_tax=row[13], tip_amount=row[14],
                                                           tolls_amount=row[15], ehail_fee=row[16],
                                                           improvement_surcharge=row[17], total_amount=row[18],
                                                           payment_type=fare_data.get('payment_type'))
                time_data = loadHelper.get_time_data(row[1])
                pickup_time = models.TaxiDatetime.objects.create(taxi_date=row[1], year=time_data.get('year'),
                                                                 month=time_data.get('month'),
                                                                 month_of_year=time_data.get('month_of_year'),
                                                                 week_of_year=time_data.get('week_of_year'),
                                                                 day=time_data.get('day'),
                                                                 day_of_week=time_data.get('day_of_week'),
                                                                 day_of_month=time_data.get('day_of_month'),
                                                                 day_of_year=time_data.get('day_of_year'),
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
                models.TaxiFare.objects.create(fare_pickup_location=pickup_location,
                                               fare_dropoff_location=dropoff_location,
                                               vendor_info=vendor_info,
                                               store_and_forward_info=store_and_forward_info,
                                               rate_code_info=rate_code_info,
                                               additional_fare_info=fare_info,
                                               fare_pickup_time=pickup_time,
                                               fare_dropoff_time=dropoff_time,)
    return HttpResponse("<!DOCTYPE html><html><body><h1>The data was loaded successfully!</h1></body></html>")


def load_taxi_fare(request, taxi_fare_id):
    try:
        taxi_fare = models.TaxiFare.objects.get(pk=taxi_fare_id)
    except models.TaxiFare.DoesNotExist:
        raise Http404("Taxi Fare does not exist")
    return render(request, 'dataload/taxifare.html', {'taxi_fare': taxi_fare})


def load_fare_info(request, fare_info_id):
    try:
        fare_info = models.FareInfo.objects.get(pk=fare_info_id)
    except models.FareInfo.DoesNotExist:
        raise Http404("Fare Info does not exist")
    return render(request, 'dataload/fareinfo.html', {'fare_info': fare_info})
