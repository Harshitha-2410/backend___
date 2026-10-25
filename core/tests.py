from django.test import TestCase
from rest_framework.test import APIClient


class ApiEndpointBehaviorTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root_is_public(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('endpoints', response.json())

    def test_auth_routes_accept_get_for_metadata(self):
        for path in ['/api/login/', '/api/register/']:
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200)
            self.assertIn('message', response.json())
