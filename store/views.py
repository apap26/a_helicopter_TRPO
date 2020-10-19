from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json
import store.models
from store import models


def index(request):
    return render(request, "index.html", {})


def product_place(request, product, brand=None):
    return -1


def product(request, id):
    return -2


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


def api_products(request, category, brand=None):
    POSX = 'POSX'
    LENGS = 'LENGS'
    a = 1
    if (request.GET.get(POSX) != None and request.GET.get(LENGS) != None):
        try:
            start = int(request.GET.get(POSX))
            limit = int(request.GET.get(LENGS))
            js = products_to_json(start, start+limit, category, brand)
            return HttpResponse(js)
        except:
            js = products_to_json(0, 100, category, brand)
            return HttpResponse(js)
    else:
        js = products_to_json(0, 100, category, brand)
        return HttpResponse(js)


def products_to_json(start, end, category, brand = None):
    product = models.product.objects.raw(
        "select * FROM `store_product` where cat_id_id = {0} order by id desc limit {1}, {2}".format(category,
                                                                                                     start,
                                                                                                     end))
    # Я имал djang овскую подстановку с защитой от sql инъекций, фигли то оно не работает, шатал я его дом изба
    # пускай ОбстрОктные хаЦкеры ломают этот сайт, я имал этот дом изба!!!
    result = []
    for i in product:
        result.append({'id': i.id, 'name': i.name, 'price':  float(i.price),
                       'image': i.image.url, 'about': i.about, 'brand_id': i.brand_id})
    js = json.dumps(result)
    return js


### HARDCODE BLOCK


def about(request):
    ret = render(request, 'about.html', {})
    return ret
# Create your views here.
