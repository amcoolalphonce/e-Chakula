from django.contrib import admin
from .models import Pizza, Beverages, Dishes, Special

class PizzaAdmin(admin.ModelAdmin):
        list_display = ('name', 'priceL', 'priceM')

admin.site.register(Pizza, PizzaAdmin)

class BeveragesAdmin(admin.ModelAdmin):
        list_display = ('name', 'price')

admin.site.register(Beverages, BeveragesAdmin)

class DishesAdmin(admin.ModelAdmin):
        list_display = ('name', 'price')

admin.site.register(Dishes, DishesAdmin)

class SpecialAdmin(admin.ModelAdmin):
        list_display = ('name', 'price')

admin.site.register(Special, SpecialAdmin)


