
from django.urls import path
from florist import views

from django.contrib import admin 
urlpatterns = [
    path('pedido/', views.pedido_form, name='pedido_form'),
    path('buscar_pedido/', views.buscar_pedido, name='buscar_pedido'),
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
]

