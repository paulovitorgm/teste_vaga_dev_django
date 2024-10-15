from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class TestIndex(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
