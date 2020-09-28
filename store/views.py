from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json
import store.models


def index(request):
    return render(request, "index.html", {})


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
    # category = store.models.category.get(id=category)
    # brand = store.models.brand.
    product = store.models.product.objects.get(cat_id=category) if brand == None else models.product.objects.get(cat_id=category, brand=brand)
    json_product = serializers.serialize("xml", product)

    return HttpResponse(json_product)

# Create your views here.
