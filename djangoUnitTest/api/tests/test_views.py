from django.test import TestCase

from rest_framework.test import APIRequestFactory
from api.models import SampleTable

from api.views import SampleGet


class APIViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        SampleTable.objects.create(name="testName", phone="000")
        SampleTable.objects.create(name="sampleName", phone=111)

    def test_sample_get_api(self):
        factory = APIRequestFactory()
        view = SampleGet.as_view()
        url = "http://127.0.0.1:8000/api/sampleget"
        request = factory.get(url)

        response = view(request)
        self.assertEquals(len(response.data), 2)
        self.assertEquals(response.data[0]["name"], "testName")
        self.assertEquals(response.data[1]["phone"], 111)
