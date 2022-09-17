from django.contrib import admin

from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}
