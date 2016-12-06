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

    man_count = borough_get(cursor, 'Manhattan')
    bron_count = borough_get(cursor, 'Bronx')
    que_count = borough_get(cursor, 'Queens')
    brook_count = borough_get(cursor, 'Brooklyn')
    sta_count = borough_get(cursor, 'Staten')

    borough_counts = {'Manhattan': man_count, 'Bronx': bron_count,
                      'Queens': que_count, 'Brooklyn': brook_count,
                      'Staten': sta_count}

    ordered_counts = sorted(borough_counts.items(), key=lambda x:x[1])
    ordered_counts.reverse()
    return render(request, 'driver/boroughs.html', {'ordered_counts': ordered_counts})


def borough_get(cursor, borough):
    cursor = connection.cursor()
    cursor.execute(
        "select count(a.id) from dataload_taxifare a, dataload_taxilocation b where a.fare_pickup_location_id = b.id and b.borough = %s", [borough])
    return cursor.fetchone()[0]


def boroughs_by_week(request, week):
    cursor = connection.cursor()

    man_count = borough_get_by_week(cursor, 'Manhattan', week)
    bron_count = borough_get_by_week(cursor, 'Bronx', week)
    que_count = borough_get_by_week(cursor, 'Queens', week)
    brook_count = borough_get_by_week(cursor, 'Brooklyn', week)
    sta_count = borough_get_by_week(cursor, 'Staten', week)

    borough_counts = {'Manhattan': man_count, 'Bronx': bron_count,
                      'Queens': que_count, 'Brooklyn': brook_count,
                      'Staten': sta_count}

    ordered_counts = sorted(borough_counts.items(), key=lambda x:x[1])
    ordered_counts.reverse()
    return render(request, 'driver/boroughs_by_week.html', {'ordered_counts': ordered_counts, 'week': week})


def borough_get_by_week(cursor, borough, week):
    cursor = connection.cursor()
    cursor.execute(
        "select count(a.id) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c where a.fare_pickup_location_id = b.id and a.fare_pickup_time_id = c.id and b.borough = %s and c.week_of_year = %s", [borough, week])
    return cursor.fetchone()[0]


def average_borough_fare(request, borough):

    if borough in ['Manhattan', 'Bronx', 'Queens', 'Brooklyn', 'Staten']:
        cursor = connection.cursor()

        avg_22 = borough_avg_get(cursor, borough, 22)
        avg_23 = borough_avg_get(cursor, borough, 23)
        avg_24 = borough_avg_get(cursor, borough, 24)
        avg_25 = borough_avg_get(cursor, borough, 25)
        avg_26 = borough_avg_get(cursor, borough, 26)

        weeks = {'22': avg_22, '23': avg_23, '24': avg_24, '25': avg_25, '26': avg_26}

        ordered_weeks = collections.OrderedDict(sorted(weeks.items()))

        average = {'borough': borough, 'weeks': ordered_weeks}

        return render(request, 'driver/borough_average.html', {'average': average})
    else:
        raise Http404("Taxi Fare does not exist")


def borough_avg_get(cursor, borough, week):
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = %s and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = %s",
        [borough, week])
    return Decimal(format(cursor.fetchone()[0], '.2f'))


def best_day(request, week):
    if int(week) in range(0, 52):
        cursor = connection.cursor()

        sunday_total = best_day_get(cursor, 'Sunday', week)
        monday_total = best_day_get(cursor, 'Monday', week)
        tuesday_total = best_day_get(cursor, 'Tuesday', week)
        wednesday_total = best_day_get(cursor, 'Wednesday', week)
        thursday_total = best_day_get(cursor, 'Thursday', week)
        friday_total = best_day_get(cursor, 'Friday', week)
        saturday_total = best_day_get(cursor, 'Saturday', week)

        day_totals = {'Sunday': sunday_total, 'Monday': monday_total, 'Tuesday': tuesday_total,
                      'Wednesday': wednesday_total, 'Thursday': thursday_total, 'Friday': friday_total,
                      'Saturday': saturday_total}

        ordered_day_totals = collections.OrderedDict(sorted(day_totals.items()))

        context = {'week': week, 'days': ordered_day_totals}
        return render(request, 'driver/day.html', context)
    else:
        raise Http404("Taxi Fare does not exist")


def best_day_get(cursor, day, week):
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = %s and c.week_of_year = %s",
        [day, week])
    return cursor.fetchone()[0]
