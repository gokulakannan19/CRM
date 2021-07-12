from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html', context={})


def customer(request):
    return render(request, 'accounts/customer.html', context={})


def products(request):
    return render(request, 'accounts/products.html', context={})
