from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json
import store.models
from store import models


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
    product = store.models.product.objects.all().filter(cat_id=category) if brand is None else models.product.objects.all().filter(cat_id=category, brand=brand)
    json_product = serializers.serialize("json", product)
    return HttpResponse(json_product)


def api_new(request):
    # . Новинки на главной странице

    return HttpResponse("todo")


def api_brand(request):
    brands = models.brand.objects.all()
    return HttpResponse(serializers.serialize("json", brands))


def api_pop(request):
    return -1


def api_category(request):
    categories = models.category.objects.all()
    result = []
    for i in categories:
        result.append({'id': i.id, 'name': i.name, 'url': '/product/' + i.name + "/"})
    js = json.dumps(result)
    return HttpResponse(js)


def api_products(request):
    return 437
# Create your views here.
