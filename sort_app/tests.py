from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
import random as r

class Test(TestCase):
    def test_generate_array(self):
        number = r.randrange(10, 45)
        response = self.client.post(
            reverse('generate_array'),
            data={'size': str(number)},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(200, response.status_code)
        array_str = response.content.decode('ascii').replace('[', '').replace(']', '').replace(',', '')
        array = list(array_str.split(" "))         
        self.assertEqual(len(array), number)
