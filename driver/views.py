from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('This is the driver view')

def recent(request):
    response = "This is the most recent endpoint"
    return HttpResponse(response)