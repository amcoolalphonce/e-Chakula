from django.shortcuts import render
from django.http import HttpResponse
from.models import Pizza, Dishes, Special, Beverages


def index(request):
        return render(request, 'food/index.html')

def pizza(request):
        pizzas = Pizza.objects.all()
        context = { 'pizzas' : pizzas}
        return render(request, 'food/pizza.html', context)

def beverages(request):
        beverages = Beverages.objects.all()
        context = {'beverages' : beverages}
        return render(request, 'food/beverages.html', context)