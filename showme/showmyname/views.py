from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_my_name(request):
    return HttpResponse("Hello, my name is Django!")