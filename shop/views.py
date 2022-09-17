from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm


def main(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'shop/category.html', context)


def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, available=True)
    cart_product_form = CartAddProductForm()
    context = {'category': category,
               'products': products,
               'cart_product_form': cart_product_form}
    return render(request, 'shop/list.html', context)


def product_view(request, id, product_slug):
    product = get_object_or_404(Product,
                                id=id,
                                available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product,
               'cart_product_form': cart_product_form}
    return render(request, 'shop/product.html', context)
