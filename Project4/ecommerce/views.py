from django.shortcuts import render
from django.utils import timezone

from .models import Order, OrderItem, Product, Client


def home(request):

    products = Product.objects.all()
    context = {'products':products, 'cartItems': None}
    return render(request, 'ecommerce/home.html', context)


def cart(request, **kwargs):
	items = []
	user_pk = request.session.get('user_id')
	
	if not user_pk:
		return render(request, 'ecommerce/cart.html', {'items': items})
	
	client = Client.objects.filter(user_id=user_pk).first()
	order = Order.objects.filter(client_id=client.pk, completed_at__isnull=True).first()
	
	if request.method.lower() == 'get' and order:
		items = order.items
	elif request.method.lower() == 'post':
		if order:
			product = Product.objects.filter(pk=kwargs.get('pk')).first()
			order_item = OrderItem.objects.create(**{'product_id': product.pk, 'product_value': product.price, 'order_id': order.pk, 'client_id': client.pk, 'product_add_at': timezone.now()})
		else:
			# criar a order e adicionar o order item
			client
			create_order = Order.objects.create(**{'client_id': client.id, 'client_email': client.email})
			product = Product.objects.filter(pk=kwargs.get('pk')).first()
			order_item = OrderItem.objects.create(**{'product_id': product.pk, 'product_value': product.price, 'quantity': 2, 'order_id': create_order.pk, 'client_id': client.pk, 'product_add_at': timezone.now()})

		if order_item:
			items = order.items
	
	context = {'items': items, 'order': order}
	return render(request, 'ecommerce/cart.html', context)


def checkout(request, **kwargs):
	items = OrderItem.objects.all()
	order = Order.objects.filter(pk=2).first()

	context = {'items': items, 'order': order}
	return render(request, 'ecommerce/checkout.html', context)

def delete(request, **kwargs):
	order_id = request.POST.get('order_id')
	item_id = kwargs.get('pk')

	if OrderItem.objects.filter(pk=item_id).exists():
		item = OrderItem.objects.filter(pk=item_id).first()	
		item.delete()

	items = OrderItem.objects.filter(order_id=order_id)
	context = {'items': items, 'order': item.order}
	return render(request, 'ecommerce/cart.html', context)

