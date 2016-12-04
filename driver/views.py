from django.shortcuts import render
from django.http import HttpResponse
from dataload.models import TaxiFare


# Create your views here.
def index(request):
    # return HttpResponse('This is the driver view')
    return render(request, 'driver/index.html', None)


def recent(request):
    recent_fare_list = TaxiFare.objects.order_by('-id')[:100]
    context = {'recent_fare_list': recent_fare_list}
    return render(request, 'driver/recent/recent.html', context)
