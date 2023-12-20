from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
        list_display = ('name', 'priceL', 'priceM')


admin.site.register(Pizza, PizzaAdmin)
