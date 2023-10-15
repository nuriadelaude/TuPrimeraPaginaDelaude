from django.db import models

class Pedido(models.Model):
    customer_name = models.CharField(max_length=100)
    flower_type = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Pedido {self.id}"

