from django.contrib import admin

from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number',
                       'date',
                       'delivery_cost',
                       'order_total',
                       'grand_total',)

    fields = ('customer',
              'stripe_pid',
              'order_number',
              'date',
              'full_name',
              'email',
              'phone_number',
              'street_address_1',
              'street_address_2',
              'town',
              'postcode',
              'delivery_cost',
              'order_total',
              'grand_total')

    list_display = ('order_number',
                    'date',
                    'full_name',
                    'delivery_cost',
                    'order_total',
                    'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

# admin.site.register(OrderLineItem)
