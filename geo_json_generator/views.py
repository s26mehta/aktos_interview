from django.http import HttpResponse
from django.shortcuts import render

from .utils import helper_functions as helpers
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='1000/h')
def index(request, min_previous_jobs_count = 0, max_previous_jobs_count = 2^16, status = None):
    helpers.process_csv_data()
    geo_data = helpers.get_consumers(min_previous_jobs_count, max_previous_jobs_count, status)

    context = {
        "geo_data": geo_data,
    }
    
    return HttpResponse(geo_data)



