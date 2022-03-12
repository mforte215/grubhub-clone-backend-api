from ast import Or
from django.contrib import admin

from app.models import CustomUser, FoodItem, Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem

class UserOrdersInLine(admin.TabularInline):
    model = Order

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_by', 'created_at')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('orderid', 'fooditemid', 'quantity', 'total_price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_by', 'order_at', 'total_price')
    inlines = [OrderItemInLine,]

class CustomUserAdmin(admin.ModelAdmin):
    inlines = [UserOrdersInLine,]


admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
