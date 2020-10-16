from django.urls import path
from django.views.generic import RedirectView

from store import views

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    path('', views.index),
    path('product/id<int:id>', views.product),
    path('product/<int:category>/<int:brand>/', views.product_place),
    path('product/<int:category>/', views.product_place),
    path('brand/', views.brand),
    # path('brand/<str:brand>/', views.brand_page),
    path('api/get_product/<int:category>/',views.api_get_product),
    path('api/get_product/<int:category>/<int:brand>/', views.api_get_product),
    path('api/new/', views.api_new),
    path('api/brand/', views.api_brand),
    path('api/popular/', views.api_pop),
    path('api/category/', views.api_category),
    path('api/product/<int:cat_id>/', views.api_products),
    ### HARDCODE BLOCK
    path("about", views.about)
]
