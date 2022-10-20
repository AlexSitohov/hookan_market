from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import *
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:
                product = item['product']
                quantity = item['quantity']
                product_to_change = Product.objects.get(name=product.name)
                try:
                    product_to_change.stock -= quantity
                    product_to_change.save()
                    if product_to_change.stock == 0:
                        product_to_change.available = False
                        product_to_change.save()

                except:
                    cart.clear()
                    form.clean()
                    return redirect('order_create')

                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'], )

                print('!!!!!!!!!!!!!!!!!!!!!!!!', cart.get_total_price())

            # очистка корзины
            cart.clear()
            form.clean()
            return redirect('main')
            # return HttpResponse(f'Ваш закакз - {order.pk}')
            # return render(request, 'orders/order/created.html',
            #               {'order': order})
    else:
        form = OrderCreateForm

    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})
