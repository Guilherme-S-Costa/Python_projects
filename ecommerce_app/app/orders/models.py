from django.db import models
from django.contrib.auth.models import User

from app.common import choices

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor total', default=0.0)
    status = models.CharField( max_length=50, choices=choices.ORDER_STATUS, verbose_name='Status do pedido', default='created')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self) -> str:
        return f"Pedido N. {self.pk} | {self.user.pk }"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Id do pedido', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', verbose_name='Id do pedido', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=190, verbose_name='Nome do produto', null=True, blank=True)
    variation_product = models.ForeignKey('products.Variation', verbose_name='Id da variação do produto', on_delete=models.SET_NULL, null=True, blank=True)
    variation_produtcts_name = models.CharField(max_length=190, null=True, blank=True, verbose_name='Variação do produto')
    amount = models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Valor', default=0.0)
    quantity = models.PositiveBigIntegerField(verbose_name='Quantidade')
    image = models.CharField(max_length=2000)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Items dos pedidos'

    def __str__(self) -> str:
        return f" Item {self.pk} | {self.order_id} | {self.variation_product}"