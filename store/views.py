import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import serializers
import json
import store.models
from store import models
from django.utils import timezone, dateformat
from django.core.exceptions import ObjectDoesNotExist

"""
Динамическая вёрстка
"""


def e404(request):
    return HttpResponse("404")


def index(request):
    new = models.product.objects.order_by('date_add')[6:]
    popular = models.product.objects.filter(is_popular=True)[6:]
    if(new.count() < 6 | popular.count() < 6):
        return render(request, "index.html", {})
    popular_1 = popular[0]
    popular_2 = popular[1]
    popular_3 = popular[2]
    popular_4 = popular[3]
    popular_5 = popular[4]
    popular_6 = popular[5]
    new_1 = new[0]
    new_2 = new[1]
    new_3 = new[2]
    new_4 = new[3]
    new_5 = new[4]
    new_6 = new[5]
    return render(request, "index.html", {'pop1':popular_1,'pop2':popular_2,
                                          'pop3':popular_3, 'pop4':popular_4,
                                          'pop5':popular_5, 'pop6':popular_6,
                                          'new_1':new_1, 'new_2':new_2,
                                          'new_3':new_3, 'new_4':new_4,
                                          'new_5':new_5, 'new_6':new_6})


def manager_admin(request):


    return render(request, "base_extended_oth.html", {})


def register(request):
    if (request.method == 'POST'):
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            country_id = int(request.POST.get('countryid'))
            second_name = request.POST.get('secondname')
            first_name = request.POST.get('firstname')
            middle_name = request.POST.get('middlename')
            phone = request.POST.get('phone')

            new_user = User(username=username, email=email, password=password)
            new_user.save()
            peson = models.pesons(id_country_id=country_id, second_name=second_name, first_name=first_name,
                                  middle_name=middle_name, phone=phone, user_t=new_user)
            peson.save()
            request.user = new_user
            print("Succes!")
            return render(request, "reg.html", {'error':'Регистрация успешно выполнена'})
        except Exception:
            return render(request, "reg.html", {'error':'Ошибка, возможно это имя пользователя уже занято'})
    else:
        return render(request, "reg.html", {})



def buy(request):
    try:
        id = int(request.GET.get('id'))
        product = models.product.objects.get(id=id)
        # if not request.user.is_anonymous:
        user = request.user
        return render(request, "order.html", {'product':product, 'user':user})
    except Exception:
        return e404(request)

def accept_buy(request):
    try:
        if request.user.is_anonymous:
            return e404(request)
        phone = request.POST.get('phone')
        adres = request.POST.get('address')
        id = int(request.POST.get('id'))
        product = models.product.objects.get(id=id)
        sale = models.sale(user=models.pesons.objects.get(user_t=request.user), payments_method_id=3, id_staff_id=3)
        sale.save()
        check_pos = models.sale_pos(id_sale=sale, count=1, id_product_id=product.id, price=product.price)
        check_pos.save()
        return render(request, "order_is_processed.html")
    except ZeroDivisionError:
        return e404(request)


def product_place(request, category, brand=None):
    try:
        category = models.category.objects.get(id=category)
        products = models.product.objects.filter(cat_id=category) if brand == None else models.product.objects.filter(cat_id=category, brand_id=brand)
        count_product = products.count()
        return render(request, "select_category.html", {'category':category, 'products':products, 'count':count_product})
    except ObjectDoesNotExist:
        return e404(request)


def product(request, id):
    try:
        product = models.product.objects.get(id=int(id))
        return render(request, "product.html", {'product':product})
    except ObjectDoesNotExist:
        return HttpResponse("404")


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
    return render(request, 'about.html', {})


def payment(request):  # Об плате
    return render(request, 'payment.html', {})


def delivery(request):  # Доставка
    return render(request, 'delivery.html', {})



def warranty(request):  # Гарантия
    return render(request, 'warranty.html', {})

