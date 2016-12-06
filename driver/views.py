from django.shortcuts import render
from decimal import Decimal
from django.http import HttpResponse, Http404
from dataload.models import TaxiFare
from django.db import connection

import collections


# Create your views here.
def index(request):
    # return HttpResponse('This is the driver view')
    return render(request, 'driver/index.html', None)


def recent(request):
    recent_fare_list = TaxiFare.objects.order_by('-id')[:100]
    context = {'recent_fare_list': recent_fare_list}
    return render(request, 'driver/recent.html', context)


def boroughs(request):
    cursor = connection.cursor()

    cursor.execute("select count(a.id) from dataload_taxifare a, dataload_taxilocation b where a.fare_pickup_location_id = b.id and b.borough = 'Manhattan'")
    man_count = cursor.fetchone()[0]
    cursor.execute("select count(a.id) from dataload_taxifare a, dataload_taxilocation b where a.fare_pickup_location_id = b.id and b.borough = 'Bronx'")
    bron_count = cursor.fetchone()[0]
    cursor.execute("select count(a.id) from dataload_taxifare a, dataload_taxilocation b where a.fare_pickup_location_id = b.id and b.borough = 'Queens'")
    que_count = cursor.fetchone()[0]
    cursor.execute("select count(a.id) from dataload_taxifare a, dataload_taxilocation b where a.fare_pickup_location_id = b.id and b.borough = 'Brooklyn'")
    brook_count = cursor.fetchone()[0]
    cursor.execute("select count(a.id) from dataload_taxifare a, dataload_taxilocation b where a.fare_pickup_location_id = b.id and b.borough = 'Staten'")
    sta_count = cursor.fetchone()[0]

    borough_counts = {'Manhattan': man_count, 'Bronx': bron_count,
                      'Queens': que_count, 'Brooklyn': brook_count,
                      'Staten': sta_count}

    ordered_counts = sorted(borough_counts.items(), key=lambda x:x[1])
    ordered_counts.reverse()
    return render(request, 'driver/boroughs.html', {'ordered_counts': ordered_counts})


def average_borough_fare(request, borough):

    if borough in ['Manhattan', 'Bronx', 'Queens', 'Brooklyn', 'Staten']:
        cursor = connection.cursor()

        cursor.execute(
            "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = %s and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 22", [borough])
        avg_22 = Decimal(format(cursor.fetchone()[0], '.2f'))
        cursor.execute(
            "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = %s and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 23", [borough])
        avg_23 = Decimal(format(cursor.fetchone()[0], '.2f'))
        cursor.execute(
            "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = %s and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 24", [borough])
        avg_24 = Decimal(format(cursor.fetchone()[0], '.2f'))
        cursor.execute(
            "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = %s and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 25", [borough])
        avg_25 = Decimal(format(cursor.fetchone()[0], '.2f'))
        cursor.execute(
            "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = %s and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 26", [borough])
        avg_26 = Decimal(format(cursor.fetchone()[0], '.2f'))

        weeks = {'22': avg_22, '23': avg_23, '24': avg_24, '25': avg_25, '26': avg_26}

        ordered_weeks = collections.OrderedDict(sorted(weeks.items()))

        average = {'borough': borough, 'weeks': ordered_weeks}

        return render(request, 'driver/borough_average.html', {'average': average})
    else:
        raise Http404("Taxi Fare does not exist")


def best_day(request):
    cursor = connection.cursor()

    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Sunday' and c.week_of_year = 23")
    sunday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Monday' and c.week_of_year = 23")
    monday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Tuesday' and c.week_of_year = 23")
    tuesday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Wednesday' and c.week_of_year = 23")
    wednesday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Thursday' and c.week_of_year = 23")
    thursday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Friday' and c.week_of_year = 23")
    friday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Saturday' and c.week_of_year = 23")
    saturday_total = cursor.fetchone()[0]

    day_totals = {'Sunday': sunday_total, 'Monday': monday_total, 'Tuesday': tuesday_total,
                  'Wednesday': wednesday_total, 'Thursday': thursday_total, 'Friday': friday_total,
                  'Saturday': saturday_total}

    ordered_day_totals = collections.OrderedDict(sorted(day_totals.items()))
    return render(request, 'driver/day.html', {'ordered_totals': ordered_day_totals})
