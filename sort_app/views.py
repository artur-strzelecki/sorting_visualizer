from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from methods.insertion_sort import insertion_sort
from methods.bubble_sort import bubble_sort
from generate_array import generate_array
import json

def index(request):
    return render(request, 'index.html')

def insertion_sort_view(request):
    array = generate_array(30)
    sort_return = []
    for array in insertion_sort(array):
        sort_return.extend([list(array)])

    sort_json = json.dumps(sort_return)
    return HttpResponse(sort_json)

