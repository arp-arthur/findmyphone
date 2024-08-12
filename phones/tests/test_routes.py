from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from phones.models import Phone

# Create your tests here.
class PhoneAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="test_phone", password="pass")
        self.client.force_login(user=self.user)
        self.phone = Phone.objects.create(phone_model="Xiaomi", user=self.user)

    def test_create_phone(self) -> None:
        url = reverse("phone-list")
        data = {
            "phone_model": "Samsung Galaxy X"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Phone.objects.count(), 2)
        self.assertEqual(Phone.objects.last().phone_model, "Samsung Galaxy X")

    def test_list_phone(self) -> None:
        url = reverse("phone-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(Phone.objects.last().phone_model, "Xiaomi")