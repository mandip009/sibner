import requests
from json import dumps

from property.response import error_explaination
from property.utils import generate_valuation_api_url


def get_property_details(request_data):
    response_data = {"status": "failed", "code": 400, "message": "Something went wrong"}
    try:
        url = generate_valuation_api_url(request_data)
        response = requests.get(url=url)
        if not response.ok:
            response_data = response.json()
            response_data["description"] = error_explaination.get(response_data.get("code", ""), "Information not available")
            response._content = dumps(response_data).encode()
    except Exception as exception:
        response_data = {"status": "error", "code": 500, "message": "Internal server error : " + str(exception)}
        response._content = dumps(response_data).encode()

    return response
