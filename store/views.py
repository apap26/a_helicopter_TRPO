from django.http import HttpResponse
from django.shortcuts import render
import json


def index(request):
    return 0


def product_place(request, product, brand=None):
    return render(request, "select_category.html", {})


def product(request, id):
	return -1


def brand(request):
    return -8


def brand_page(request, brand):
    return -3

# --------------------------------------------------------------------------------------------------------------------

def api(request):
    return HttpResponse("?")


def api_get_product(request, category, brand=None):
    
    return 8

# Create your views here.
