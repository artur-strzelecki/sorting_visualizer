from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
import random as r
from generate_array import generate_array

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


    def test_insertion_sort(self):
        response = self.client.post(
            reverse('insertion_sort'),
            data={'array[]': generate_array(10)},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )     
        self.assertEqual(200, response.status_code)
        array_str = response.content.decode('ascii').replace('[', '').replace(']', '').replace(',', '')
        array = list(array_str.split(" "))  
        array.reverse()
        array_last = array[0:10]
        array_last.reverse()
        self.assertEqual(array_last, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

    def test_bubble_sort(self):
        response = self.client.post(
            reverse('bubble_sort'),
            data={'array[]': generate_array(10)},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )     
        self.assertEqual(200, response.status_code)
        array_str = response.content.decode('ascii').replace('[', '').replace(']', '').replace(',', '')
        array = list(array_str.split(" "))  
        array.reverse()
        array_last = array[0:10]
        array_last.reverse()
        self.assertEqual(array_last, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])   

    def test_odd_even_sort(self):
        response = self.client.post(
            reverse('odd_even_sort'),
            data={'array[]': generate_array(10)},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )     
        self.assertEqual(200, response.status_code)
        array_str = response.content.decode('ascii').replace('[', '').replace(']', '').replace(',', '')
        array = list(array_str.split(" "))  
        array.reverse()
        array_last = array[0:10]
        array_last.reverse()
        self.assertEqual(array_last, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']) 

    def test_selection_sort(self):
        response = self.client.post(
            reverse('selection_sort'),
            data={'array[]': generate_array(10)},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )     
        self.assertEqual(200, response.status_code)
        array_str = response.content.decode('ascii').replace('[', '').replace(']', '').replace(',', '')
        array = list(array_str.split(" "))  
        array.reverse()
        array_last = array[0:10]
        array_last.reverse()
        self.assertEqual(array_last, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']) 