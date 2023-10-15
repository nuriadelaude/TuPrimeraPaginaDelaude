from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['customer_name', 'flower_type', 'quantity']

class BuscarPedidoForm(forms.Form):
    customer_name = forms.CharField(label='Nombre del Cliente', max_length=100)