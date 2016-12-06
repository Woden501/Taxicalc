from decimal import Decimal
from datetime import datetime

BOROUGH_LATS = {'Manhattan': 40.7831, 'Bronx': 40.8448, 'Queens': 40.7282,
                'Brooklyn': 40.6782, 'Staten': 40.5795}

BOROUGH_LONS = {'Manhattan': -73.9712, 'Bronx': -73.8648, 'Queens': -73.7949,
                'Brooklyn': -73.9442, 'Staten': -74.1502}


def get_vendor_name(vendor_id):
    vendor_int = int(vendor_id)
    if vendor_int is 1:
        vendor_name = 'Creative Mobile Technologies'
    elif vendor_int is 2:
        vendor_name = 'VeriFone Inc.'
    else:
        vendor_name = 'Unknown'
    return vendor_name


def get_fare_data(trip_type_id, payment_type_id):
    trip_type_int = int(trip_type_id)
    payment_type_int = int(payment_type_id)

    if trip_type_int is 1:
        trip_type = 'street-hail'
    elif trip_type_int is 2:
        trip_type = 'dispatch'
    else:
        trip_type = 'unknown'

    if payment_type_int is 1:
        payment_type = 'credit card'
    elif payment_type_int is 2:
        payment_type = 'cash'
    elif payment_type_int is 3:
        payment_type = 'no charge'
    elif payment_type_int is 4:
        payment_type = 'dispute'
    elif payment_type_int is 5:
        payment_type = 'unknown'
    elif payment_type_int is 6:
        payment_type = 'voided trip'
    else:
        payment_type = 'unknown'

    return {'trip_type': trip_type, 'payment_type': payment_type}


def get_time_data(value):
    the_datetime = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    year = the_datetime.strftime('%Y')
    month = the_datetime.strftime('%B')
    month_of_year = the_datetime.strftime('%m')
    week_of_year = the_datetime.strftime('%U')
    day = the_datetime.strftime('%A')
    day_of_week = the_datetime.strftime('%w')
    day_of_month = the_datetime.day
    day_of_year = the_datetime.strftime('%j')
    hour = the_datetime.strftime('%H')
    minute = the_datetime.strftime('%M')
    second = the_datetime.strftime('%S')

    return {'year': year, 'month': month, 'month_of_year': month_of_year,
            'week_of_year': week_of_year, 'day': day, 'day_of_week': day_of_week,
            'day_of_month': day_of_month, 'day_of_year': day_of_year, 'hour': hour,
            'minute': minute, 'second': second}


def is_valid(row):
    if len(row) is not 21:
        return False

    for item in row:
        if item is None:
            return False

    return True


def get_borough(latitude, longitude):
    latitude = Decimal(latitude)
    longitude = Decimal(longitude)
    borough = find_nearest(BOROUGH_LATS, latitude)

    return borough


def find_nearest(the_dictionary, the_value):
    smallest_difference = None
    smallest_key = None

    for key, value in the_dictionary.iteritems():
        difference = abs(Decimal(value) - the_value)

        if smallest_difference is None or difference < smallest_difference:

            smallest_difference = difference
            smallest_key = key

    return smallest_key


def find_rate_info(rate_code_id):
    rate_value = int(rate_code_id)
    if rate_value is 1:
        info = {'group': 'standard', 'type': 'standard'}
    elif rate_value is 2:
        info = {'group': 'location', 'type': 'JFK'}
    elif rate_value is 3:
        info = {'group': 'location', 'type': 'Newark'}
    elif rate_value is 4:
        info = {'group': 'location', 'type': 'Nassau or Westchester'}
    elif rate_value is 5:
        info = {'group': 'other', 'type': 'negotiated fare'}
    elif rate_value is 6:
        info = {'group': 'other', 'type': 'group ride'}
    else:
        info = {'group': 'unknown', 'type': 'unknown'}
    return info


# def find_time_info():
#
