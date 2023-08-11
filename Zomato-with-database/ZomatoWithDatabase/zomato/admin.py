from django.contrib import admin
from .models import MenuItem, Order

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'price', 'availability')

@admin.register(Order)
class TakeOrder(admin.ModelAdmin):
    list_display = ('cus_name', 'price', 'order_status')
