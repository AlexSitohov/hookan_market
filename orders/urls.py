from django.urls import path

from .views import *

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('pay/', pay, name='pay'),
    # path('thank-you/', thank_you, name="thank_you")

]
