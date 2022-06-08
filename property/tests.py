from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from property.helper import get_property_details
from property.utils import generate_valuation_api_url


class ViewTests(TestCase):
    request_data = {"postcode": "OX41YB",
                    "internal_area": "828",
                    "property_type": "flat",
                    "construction_date": "pre_1914",
                    "bedrooms": "3",
                    "bathrooms": "1",
                    "finish_quality": "below_average",
                    "outdoor_space": "garden",
                    "off_street_parking": "0"}

    sample_success_response = {
        "status": "success",
        "postcode": "OX4 1YB",
        "postcode_type": "full",
        "params": {
            "property_type": "Flat",
            "construction_date": "Pre-1914",
            "internal_area": "828",
            "bedrooms": "3",
            "bathrooms": "1",
            "finish_quality": "Below average",
            "outdoor_space": "Garden",
            "off_street_parking": "0 spaces"
        },
        "result": {
            "estimate": 390000,
            "margin": 20000
        },
        "process_time": "0.40"
    }

    sample_url = settings.PROPERTY_VALUATION_API_PROTOCOL + "://" + settings.PROPERTY_VALUATION_API_HOST + '/' + settings.PROPERTY_VALUATION_API_SUB_URL + "&postcode=OX41YB&internal_area=828&property_type=flat&construction_date=pre_1914&bedrooms=3&bathrooms=1&finish_quality=below_average&outdoor_space=garden&off_street_parking=0"

    def test_index_exists(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_get_details_exists(self):
        response = self.client.get(reverse('get_details'))
        self.assertEqual(response.status_code, 200)

    def test_index_template_name_correct(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def test_view_returns_OK(self):
        response = self.client.get('/property/get-details')
        self.assertEqual(response.status_code, 200)

    def test_generate_valuation_api_url(self):
        response = generate_valuation_api_url(self.request_data)
        self.assertEqual(response, self.sample_url)

    def test_valuation_api_success(self):
        response = get_property_details(self.request_data)
        response_data = response.json()
        self.assertEqual(response.ok, True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data.get("status"), "success")
        self.assertEqual("postcode" in response_data, True)
        self.assertEqual(response_data.get("params"), self.sample_success_response.get("params"))

    def test_valuation_api_failure(self):
        response = get_property_details({})
        response_data = response.json()
        self.assertEqual(response.ok, False)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data.get("status"), "error")
        self.assertEqual("postcode" in response_data, False)
