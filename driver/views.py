from django.shortcuts import render
from decimal import Decimal
from django.http import HttpResponse
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


def average_borough_fare(request):
    cursor = connection.cursor()

    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Manhattan' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 22")
    man_22_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Manhattan' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 23")
    man_23_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Manhattan' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 24")
    man_24_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Manhattan' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 25")
    man_25_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Manhattan' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 26")
    man_26_avg = Decimal(format(cursor.fetchone()[0], '.2f'))

    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Bronx' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 22")
    bron_22_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Bronx' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 23")
    bron_23_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Bronx' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 24")
    bron_24_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Bronx' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 25")
    bron_25_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Bronx' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 26")
    bron_26_avg = Decimal(format(cursor.fetchone()[0], '.2f'))

    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Queens' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 22")
    que_22_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Queens' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 23")
    que_23_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Queens' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 24")
    que_24_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Queens' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 25")
    que_25_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Queens' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 26")
    que_26_avg = Decimal(format(cursor.fetchone()[0], '.2f'))

    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Brooklyn' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 22")
    brook_22_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Brooklyn' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 23")
    brook_23_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Brooklyn' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 24")
    brook_24_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Brooklyn' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 25")
    brook_25_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Brooklyn' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 26")
    brook_26_avg = Decimal(format(cursor.fetchone()[0], '.2f'))

    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Staten' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 22")
    sta_22_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Staten' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 23")
    sta_23_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Staten' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 24")
    sta_24_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Staten' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 25")
    sta_25_avg = Decimal(format(cursor.fetchone()[0], '.2f'))
    cursor.execute(
        "select avg(d.fare_amount) from dataload_taxifare a, dataload_taxilocation b, dataload_taxidatetime c, dataload_fareinfo d where b.borough = 'Staten' and a.fare_pickup_location_id = b.id and a.additional_fare_info_id = d.id and a.fare_pickup_time_id = c.id and c.week_of_year = 26")
    sta_26_avg = Decimal(format(cursor.fetchone()[0], '.2f'))

    man_weeks = {'22': man_22_avg, '23': man_23_avg, '24': man_24_avg, '25': man_25_avg, '26': man_26_avg}
    bron_weeks = {'22': bron_22_avg, '23': bron_23_avg, '24': bron_24_avg, '25': bron_25_avg, '26': bron_26_avg}
    que_weeks = {'22': que_22_avg, '23': que_23_avg, '24': que_24_avg, '25': que_25_avg, '26': que_26_avg}
    brook_weeks = {'22': brook_22_avg, '23': brook_23_avg, '24': brook_24_avg, '25': brook_25_avg, '26': brook_26_avg}
    sta_weeks = {'22': sta_22_avg, '23': sta_23_avg, '24': sta_24_avg, '25': sta_25_avg, '26': sta_26_avg}

    man_ordered_weeks = collections.OrderedDict(sorted(man_weeks.items()))
    bron_ordered_weeks = collections.OrderedDict(sorted(bron_weeks.items()))
    que_ordered_weeks = collections.OrderedDict(sorted(que_weeks.items()))
    brook_ordered_weeks = collections.OrderedDict(sorted(brook_weeks.items()))
    sta_ordered_weeks = collections.OrderedDict(sorted(sta_weeks.items()))

    averages = {
                    'Manhattan': man_ordered_weeks,
                    'Bronx': bron_ordered_weeks,
                    'Queens': que_ordered_weeks,
                    'Brooklyn': brook_ordered_weeks,
                    'Staten': sta_ordered_weeks
                }
    ordered_averages = collections.OrderedDict(sorted(averages.items()))

    return render(request, 'driver/boroughs_average.html', {'averages': ordered_averages})


def best_day(request):
    cursor = connection.cursor()

    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Sunday'")
    sunday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Monday'")
    monday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Tuesday'")
    tuesday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Wednesday'")
    wednesday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Thursday'")
    thursday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Friday'")
    friday_total = cursor.fetchone()[0]
    cursor.execute(
        "select sum(b.fare_amount) from dataload_taxifare a, dataload_fareinfo b, dataload_taxidatetime c where a.additional_fare_info_id = b.id and a.fare_pickup_time_id = c.id and c.day = 'Saturday'")
    saturday_total = cursor.fetchone()[0]

    day_totals = {'Sunday': sunday_total, 'Monday': monday_total, 'Tuesday': tuesday_total,
                  'Wednesday': wednesday_total, 'Thursday': thursday_total, 'Friday': friday_total,
                  'Saturday': saturday_total}

    ordered_day_totals = collections.OrderedDict(sorted(day_totals.items()))
    return render(request, 'driver/day.html', {'ordered_totals': ordered_day_totals})
