from django.contrib import admin
from .models import Order, OrderItem


# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ('product',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('order', 'product', 'price', 'quantity',)

    min_num = 1
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_total_cost', 'first_name', 'last_name', 'phone', 'paid',
                    'created', 'updated')
    list_display_links = ('id', 'get_total_cost', 'first_name', 'last_name', 'phone')
    list_filter = ('paid', 'created', 'updated')
    list_editable = ['paid']

    inlines = (OrderItemInline,)


admin.site.register(Order, OrderAdmin)
