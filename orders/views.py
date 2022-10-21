from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import *
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST' and request.POST.get('l'):
        form = OrderCreateForm(request.POST)
        flag = False

        if form.is_valid():
            for item in cart:
                product = item['product']
                quantity = item['quantity']
                product_to_change = Product.objects.get(name=product.name)
                if product_to_change.stock >= quantity:
                    flag = True
                elif product_to_change.stock < quantity:
                    flag = False
                    messages.success(request, f'В наличии нет {quantity} {product}')
                    break
            if flag == True:
                for item in cart:

                    product = item['product']
                    quantity = item['quantity']
                    product_to_change = Product.objects.get(name=product.name)

                    if product_to_change.stock >= quantity:
                        order = form.save()
                        OrderItem.objects.create(order=order,
                                                 product=item['product'],
                                                 price=item['price'],
                                                 quantity=item['quantity'], )

                        if product_to_change.stock - quantity == 0:
                            product_to_change.available = False
                        product_to_change.stock -= quantity
                        product_to_change.save()

        if request.POST.get('l'):
            cart.clear()
            form.clean()
            return redirect('main')

    if request.POST.get('n'):
        return redirect('pay')

    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html',
                      {'cart': cart, 'form': form})


def pay(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'orders/order/pay.html',
                  context)
