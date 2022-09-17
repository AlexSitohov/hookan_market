from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('<slug:category_slug>/', category_view, name='category'),
    path('<id>/<slug:product_slug>/', product_view, name='product'),
]


