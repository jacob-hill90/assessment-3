from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import office_list, kitchen_list, garage_list, livingroom_list, patio_list, featured_list
import requests, os, json
from requests_oauthlib import OAuth1
from dotenv import load_dotenv


def index(request):
    response = render(request, 'hackazon_app/index.html', {'featured_list': featured_list})
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

def products(request):
    query = request.GET.get('query')

    auth = OAuth1("7faa4d822f6b416c86bf0bac3a98e0ea", "724977a86e2b4c8c8bfadeaf491e7c97")
    endpoint = f"http://api.thenounproject.com/icon/{query}"

    API_response = requests.get(endpoint, auth=auth)
    print(API_response.content)
    JSON_API_response = json.loads(API_response.content)
    image_url = JSON_API_response['icon']['preview_url']
    return JsonResponse({'url': image_url })