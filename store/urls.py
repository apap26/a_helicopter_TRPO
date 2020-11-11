from django.contrib.auth import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path

from store import views

urlpatterns = [
    path('administartion/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile),
    path('register/', views.register),
    path('dev/', views.manager_admin),
    path('buy/', views.buy),
    path('buy/end', views.accept_buy),
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    path('', views.index),
    path('product/id<int:id>/', views.product),
    path('product/<int:category>/<int:brand>/', views.product_place),
    path('product/<int:category>/', views.product_place),

    # path('brand/<str:brand>/', views.brand_page),
    path('api/', views.api),
    path('api/get_product/<int:category>/',views.api_products),
    path('api/get_product/<int:category>/<int:brand>/', views.api_products),
    path('api/new/', views.api_new),
    path('api/brand/', views.api_brand),
    path('api/popular/', views.api_pop),
    path('api/category/', views.api_category),
    # path('api/product/<int:cat_id>/', views.api_products),
    ### HARDCODE BLOCK
    path("about", views.about),
    path("payment", views.payment),
    path("delivery", views.delivery),
    path("warranty", views.warranty),
]
