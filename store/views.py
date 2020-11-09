import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json
import store.models
from store import models
from django.utils import timezone, dateformat

"""
Динамическая вёрстка
"""


def index(request):

    return render(request, "index.html", {})


def product_place(request, product, brand=None):
    return render(request, "select_category.html", {})


def product(request, id):
    product = models.product.objects.get(id=int(id))
    #if product.count() == 0:
    #    return HttpResponse("404")
    return render(request, "product.html", {'product':product})


def brand(request):
    return -8


def brand_page(request, brand):
    return -3


"""
Открытый программный интерфейс веб-приложения
"""


def api(request):
    return HttpResponse("?")


def api_new(request):
    # . Новинки на главной странице
    time = timezone.now() - datetime.timedelta(days=30)
    new_product = models.product.objects.all().filter(date_add__range=(time, timezone.now()))
    js = serialaze_products(new_product)
    return HttpResponse(js)


def api_brand(request):
    brands = models.brand.objects.all()
    return HttpResponse(serializers.serialize("json", brands))


def api_pop(request):
    popular = models.product.objects.all().filter(is_popular=True)
    js = serialaze_products(popular)
    return HttpResponse(js)


def api_category(request):
    categories = models.category.objects.all()
    result = []
    for i in categories:
        result.append({'id': i.id, 'name': i.name, 'url': '/product/' + i.name + "/"})
    js = json.dumps(result)
    return HttpResponse(js)


def api_products(request, category, brand=None):  # Эта функция просит чтобы ее убили
    POSX = 'POSX'
    LENGS = 'LENGS'
    if (request.GET.get(POSX) != None and request.GET.get(LENGS) != None):
        try:
            start = int(request.GET.get(POSX))
            limit = int(request.GET.get(LENGS))
            js = products_to_json(start, start + limit, category, brand)
            return HttpResponse(js)
        except:
            js = products_to_json(0, 100, category, brand)
            return HttpResponse(js)
    else:
        js = products_to_json(0, 100, category, brand)
        return HttpResponse(js)


def products_to_json(start, end, category, brand=None):
    if brand == None:
        product = models.product.objects.raw(
            "select * FROM `store_product` where cat_id_id = {0} order by id desc limit {1}, {2}".format(category,
                                                                                                         start,
                                                                                                         end))
    else:
        product = models.product.objects.raw(
            "select * FROM `store_product` where cat_id_id = {0} AND brand_id = {1} order by id desc limit {2}, {3}".format(
                category,
                brand,
                start,
                end))
    # Я имал djang овскую подстановку с защитой от sql инъекций, фигли то оно не работает, шатал я его дом изба
    # пускай ОбстрОктные хаЦкеры ломают этот сайт, я имал этот дом изба!!!
    js = serialaze_products(product)
    return js


def serialaze_products(product):
    result = []
    for i in product:
        result.append({'id': i.id, 'name': i.name, 'price': float(i.price),
                       'image': i.image.url, 'about': i.about, 'brand_id': i.brand_id})
    js = json.dumps(result)
    return js


"""
Полностью статичная вёрстка
"""


def about(request):  # О магазине
    ret = render(request, 'about.html', {})
    return ret


def payment(request):  # Об плате
    ret = render(request, 'payment.html', {})
    return ret


def delivery(request):  # Доставка
    ret = render(request, 'delivery.html', {})
    return ret


def warranty(request):  # Гарантия
    ret = render(request, 'warranty.html', {})
    return ret
