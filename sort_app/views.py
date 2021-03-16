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
    else:
        return HttpResponse('')

def insertion_sort_view(request):
    array = generate_array(30)
    sort_return = []
    for array in insertion_sort(array):
        sort_return.extend([list(array)])

    sort_json = json.dumps(sort_return)
    return HttpResponse(sort_json)

def bubble_sort_view(request):
    pass

def odd_even_sort_view(request):
    pass



