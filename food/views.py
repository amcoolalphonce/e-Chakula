from django.shortcuts import render
from django.http import HttpResponse
from.models import Pizza, Dishes, Special, Beverages


def index(request):
        return render(request, 'food/index.html')

def beverages(request):
        return render(request, 'food/beverages.html')