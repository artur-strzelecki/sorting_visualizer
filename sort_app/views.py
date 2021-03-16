from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from methods.insertion_sort import insertion_sort
from methods.bubble_sort import bubble_sort
from generate_array import generate_array
import json

def index(request):
    return render(request, 'index.html')

def generate_array_view(request):
    if request.method == 'POST':
        size = request.POST['size']
        array = generate_array(int(size))
        array_json = json.dumps(array)
        return HttpResponse(array_json)
    return HttpResponse('')

def insertion_sort_view(request):
    if request.method == 'POST':
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
    pass

def odd_even_sort_view(request):
    pass



