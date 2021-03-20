from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from methods.insertion_sort import insertion_sort
from methods.bubble_sort import bubble_sort
from methods.odd_even_sort import odd_even_sort
from methods.selection_sort import selection_sort
from generate_array import generate_array
import json

def index(request):
    return render(request, 'index.html')

def generate_array_view(request):
    if request.method == 'POST' and request.is_ajax():
        size = request.POST.get('size', False)
        array = generate_array(int(size))
        array_json = json.dumps(array)
        return HttpResponse(array_json)
    return HttpResponse('')

def insertion_sort_view(request):
    if request.method == 'POST' and request.is_ajax():
        array = request.POST.getlist('array[]')
        sort_return = []

        # convert from string list to int list
        for i in range(0, len(array)): 
            array[i] = int(array[i]) 

        for array in insertion_sort(array):
            sort_return.extend([list(array)])

        sort_json = json.dumps(sort_return)
        return HttpResponse(sort_json)

    return HttpResponse('')

def bubble_sort_view(request):
    if request.method == 'POST' and request.is_ajax():
        array = request.POST.getlist('array[]')
        sort_return = []

        # convert from string list to int list
        for i in range(0, len(array)): 
            array[i] = int(array[i]) 

        for array in bubble_sort(array):
            sort_return.extend([list(array)])

        sort_json = json.dumps(sort_return)
        return HttpResponse(sort_json)

    return HttpResponse('')

def odd_even_sort_view(request):
    if request.method == 'POST' and request.is_ajax():
        array = request.POST.getlist('array[]')
        sort_return = []

        # convert from string list to int list
        for i in range(0, len(array)): 
            array[i] = int(array[i]) 

        for array in odd_even_sort(array):
            sort_return.extend([list(array)])

        sort_json = json.dumps(sort_return)
        return HttpResponse(sort_json)

    return HttpResponse('')   


def selection_sort_view(request):
    if request.method == 'POST' and request.is_ajax():
        array = request.POST.getlist('array[]')
        sort_return = []

        # convert from string list to int list
        for i in range(0, len(array)): 
            array[i] = int(array[i]) 

        for array in selection_sort(array):
            sort_return.extend([list(array)])

        sort_json = json.dumps(sort_return)
        return HttpResponse(sort_json)

    return HttpResponse('')      



