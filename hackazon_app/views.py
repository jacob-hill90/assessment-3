from http.client import HTTPResponse
from django.shortcuts import render
from django.http import  HttpResponseRedirect, JsonResponse, HttpResponse
from .models import office_list, kitchen_list, garage_list, livingroom_list, patio_list, featured_list, Item, Cart, CartItem
import requests, os, json
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist



def index(request):
    response = render(request, 'hackazon_app/index.html', {'featured_list': featured_list})
    return response

def about(request):
    response = render(request, 'hackazon_app/about.html')
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

def cart(request):
    cart_id = 1                             
    items = Item.objects.all()      
    cart = Cart.objects.get(id=cart_id)

    data  = []

    for item in items:
        item_dict = {}
        item_dict['item'] = item

        try:
            c_item = CartItem.objects.get(cart = cart, item = item)
            item_dict['quantity'] = c_item.quantity
        except:
            item_dict['quantity'] = 0

        data.append(item_dict)

        print(item_dict)
    
    return render(request, 'hackazon_app/cart.html', {'data': data} )

@csrf_exempt
def cart_item(request):
    cart_id = 1
    
    body = json.loads(request.body) 
    item_id = body['item_id']

    cart = Cart.objects.get(id = cart_id)
    item = Item.objects.get(id = item_id)

    try:
        c_item = CartItem.objects.get(cart = cart, item = item)
        c_item.quantity += 1
        c_item.full_clean()
        c_item.save()

    except:
        c_item = CartItem(cart = cart, item = item)
        c_item.full_clean()
        c_item.save()

    return  JsonResponse({'item_id': c_item.item.id, 'item_quantity': c_item.quantity})




    