from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response (how the view function works)
# request handler
# action


def home_page_view(request):
    return HttpResponse("Hello, World!")
