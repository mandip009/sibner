from django.conf import settings


def generate_valuation_api_url(request_data):
    url = settings.PROPERTY_VALUATION_API_PROTOCOL + "://" + settings.PROPERTY_VALUATION_API_HOST + '/' + settings.PROPERTY_VALUATION_API_SUB_URL
    for key in request_data.keys():
        url = url + "&" + key + "=" + request_data.get(key)
    return url
