from django.urls import path

from . import views

app_name = 'food'

urlpatterns =[
        path('',views.index, name = 'index'),
        path('pizza', views.pizza, name = 'pizza'),
        path('beverages',  views.beverages , name = 'beverages'),
]