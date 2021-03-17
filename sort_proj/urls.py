from django.contrib import admin
from django.urls import path
import sort_app.views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name='index'),
    path('generate_array/', v.generate_array_view, name='generate_array'),
    path('insertion_sort/', v.insertion_sort_view, name='insertion_sort'),
    path('bubble_sort/', v.bubble_sort_view, name='bubble_sort'),
    path('odd_even_sort/', v.odd_even_sort_view, name='odd_even_sort'),
    path('selection_sort/', v.selection_sort_view, name='selection_sort'),
]
