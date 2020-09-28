from django.urls import path
from store import views

urlpatterns = [
    path('', views.index),
    path('product/id<int:id>', views.product),
    path('product/<str:category>/<str:brand>/', views.product_place),
    path('product/<str:category>/', views.product_place),
    path('brand/', views.brand),
    path('brand/<str:brand>/', views.brand_page),
    path('api/<int:category>/',views.api_get_product),
    path('api/<int:category>/<int:brand>/', views.api_get_product)
]
