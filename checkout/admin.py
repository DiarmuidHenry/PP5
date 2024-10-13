from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'name', 'email', 'total_order_cost', 'order_datetime')
    list_filter = ('order_datetime',)
    search_fields = ('order_number', 'name', 'email')
    readonly_fields = ('order_number', 'delivery_charge', 'total_order_cost', 'order_datetime')

    def get_order_items(self, obj):
        # Display order items in a readable format
        return ', '.join([f"{item['quantity']} x Product ID {item['product_id']}" for item in obj.order_items])
    
    get_order_items.short_description = 'Order Items'

    fieldsets = (
        (None, {
            'fields': ('order_number', 'name', 'email', 'phone_number', 'address_1', 'address_2', 'city', 'county', 'post_code', 'country', 'order_datetime')
        }),
        ('Order Details', {
            'fields': ('order_items', 'delivery_charge', 'total_order_cost'),
            'classes': ('collapse',)  # Make this section collapsible
        }),
    )

admin.site.register(Order, OrderAdmin)
