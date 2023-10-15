from django.shortcuts import render, get_object_or_404
from .forms import PedidoForm 
from .models import Pedido 
from django.contrib import messages
from django.shortcuts import redirect
from .forms import BuscarPedidoForm

def pedido_form(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido realizado con éxito.')
            return redirect('pedido_form')
        else:
            messages.error(request, 'Hubo un error al procesar el pedido.')
    else:
        form = PedidoForm()
    
    return render(request, 'inicio/pedido_form.html', {'form': form})

def buscar_pedido(request):
    if request.method == 'POST':
        form = BuscarPedidoForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            pedidos = Pedido.objects.filter(customer_name__icontains=customer_name)
            return render(request, 'inicio/buscar_pedido.html', {'pedidos': pedidos, 'form': form})
    else:
        form = BuscarPedidoForm()
    
    return render(request, 'inicio/buscar_pedido.html', {'form': form})

def index(request):
    pedido_form = PedidoForm()
    return render(request, 'inicio/index.html', {'pedido_form': pedido_form})