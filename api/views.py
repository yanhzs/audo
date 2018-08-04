from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
import datetime


def hello(request):
    return render_to_response("index.html")