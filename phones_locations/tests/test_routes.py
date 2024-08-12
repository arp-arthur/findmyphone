from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.test import APITestCase
from phones_locations.models import LocationHistory
from phones.models import Phone

# Create your tests here.
class LocationHistoryAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="test_location", password="pass")
        self.client.force_login(user=self.user)
        self.phone = Phone.objects.create(phone_model="Xiaomi", user=self.user)

    def test_create_location_history(self) -> None:
        url = reverse("phone_locations-list")
        data = {
            "phone_id": self.phone.id,
            "location": {"latitude": -23.5505, "longitude": -46.6333},
            "timestamp": "2024-01-01T12:00:00Z",
            "battery": 40.0,
            "wifi": "EU"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LocationHistory.objects.count(), 1)
        self.assertEqual(LocationHistory.objects.last().phone, self.phone)
        
        location = LocationHistory.objects.last().location
        expected_location = Point(-46.6333, -23.5505)
        self.assertEqual(location.x, expected_location.x)
        self.assertEqual(location.y, expected_location.y)

    def test_list_location_history(self) -> None:
        url = reverse("phone_locations-list")
        first_data = {
            "phone_id": self.phone.id,
            "location": {"latitude": -23.5505, "longitude": -46.6333},
            "timestamp": "2024-01-01T12:00:00Z",
            "battery": 40.0,
            "wifi": "EU"
        }

        second_data = {
            "phone_id": self.phone.id,
            "location": {"latitude": -23.550051, "longitude": -46.633797},
            "timestamp": "2024-01-01T12:10:00Z",
            "battery": 38.0,
            "wifi": "EU"
        }

        first_response = self.client.post(url, first_data, format="json")
        self.assertEqual(first_response.status_code, status.HTTP_201_CREATED)
        second_response = self.client.post(url, second_data, format="json")
        self.assertEqual(second_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LocationHistory.objects.count(), 2)
        self.assertEqual(LocationHistory.objects.last().phone, self.phone)

        location = LocationHistory.objects.last().location
        expected_location = Point(-46.633797, -23.550051)

        self.assertEqual(location.x, expected_location.x)
        self.assertEqual(location.y, expected_location.y)