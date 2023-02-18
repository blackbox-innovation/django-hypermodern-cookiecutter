# test file for views
import pytest
from django.test import TestCase

class TestSetup(TestCase):
    def test_django_setup(self):
        """
        Test that everything is setup and that Django is working
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'empty.html')
