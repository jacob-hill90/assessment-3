from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import office_list, kitchen_list, garage_list, livingroom_list, patio_list

def index(request):
    response = render(request, 'hackazon_app/index.html')
    return response

def about(request):
    response = render(request, 'hackazon_app/about.html')
    return response

def cart(request):
    response = render(request, 'hackazon_app/cart.html')
    return response

def search(request):
    response = render(request, 'hackazon_app/search.html')
    return response

def office(request):
    response = render(request, 'hackazon_app/office.html', {'office_list': office_list})
    return response

def kitchen(request):
    response = render(request, 'hackazon_app/kitchen.html', {'kitchen_list': kitchen_list})
    return response

def garage(request):
    response = render(request, 'hackazon_app/garage.html', {'garage_list': garage_list})
    return response

def livingroom(request):
    response = render(request, 'hackazon_app/livingroom.html', {'livingroom_list': livingroom_list})
    return response

def patio(request):
    response = render(request, 'hackazon_app/patio.html', {'patio_list': patio_list})
    return response