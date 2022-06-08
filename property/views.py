from django.http import HttpResponse
from django.shortcuts import render

from property.helper import get_property_details

""" This is open REST API, needs to be authenticated """


def index(request):
    return render(request, 'index.html')


def get_details(request):
    """
    :param request: This are the Params: { "postcode":"OX41YB", "internal_area": "828",
    "property_type": "flat", "construction_date": "pre_1914", "bedrooms": 3, "bathrooms": 1, "finish_quality": "below_average", "outdoor_space": "garden", "off_street_parking": 0}

    :return: HttpResponse : {"status":"success","postcode":"OX4 1YB","postcode_type":"full","params":{"property_type":"Flat","construction_date":"Pre-1914","internal_area":"828","bedrooms":"3","bathrooms":"1","finish_quality":"Below average","outdoor_space":"Garden","off_street_parking":"0 spaces"},"result":{"estimate":390000,"margin":20000},"process_time":"0.40"}
    """
    # TODO: request & response searialization
    # TODO: Authentication is required
    # TODO: logging

    request_params = request.GET
    response = get_property_details(request_params)
    return HttpResponse(response)
