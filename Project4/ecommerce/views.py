from django.shortcuts import render
from django.utils import timezone
# from django.http import JsonResponse

from .models import Order, OrderItem, Product
# from .utils import cookieCart, cartData, guestOrder

def home(request):

    products = Product.objects.all()
    context = {'products':products, 'cartItems': None}
    return render(request, 'ecommerce/home.html', context)


def cart(request, **kwargs):
	items = []
	client = request.user.client
	order = Order.objects.filter(client_id=client.pk, completed_at__isnull=True).first()
	
	if request.method.lower() == 'get' and order:
		items = order.items
	elif request.method.lower() == 'post':
		if order:
			product = Product.objects.filter(pk=kwargs.get('pk')).first()
			order_item = OrderItem.objects.create(**{'product_id': product.pk, 'product_value': product.price, 'quantity': 2, 'order_id': order.pk, 'client_id': client.pk, 'product_add_at': timezone.now()})
		else:
			# criar a order e adicionar o order item
			create_order = Order.objects.create(**{'clent': client.id, 'client_email': client.email, 'quantity': 1})
			product = Product.objects.filter(pk=kwargs.get('pk')).first()
			order_item = OrderItem.objects.create(**{'product_id': product.pk, 'product_value': product.price, 'quantity': 2, 'order_id': order.pk, 'client_id': client.pk, 'product_add_at': timezone.now()})

		if order_item:
			items = order.items

	context = {'items': items, 'order': order}
	return render(request, 'ecommerce/cart.html', context)


def checkout(request):
	context = {}
	return render(request, 'ecommerce/checkout.html', context)



# def checkout(request):
#         data = cartData(request)

#         cartItems = data['cartItems']
#         order = data['order']
#         items = data['items']

#     if request.user.is_authenticated:
#         client = request.user.client
#         order, created = Order.objects.get_or_create(client=client, completed_at=None)
#         items = order.orderitem_set.all()
#     else:
#         items = []  
#         order = {'get_cart_total':0, 'get_cart_item':0} 


#         context = {'items':items, 'order':order, 'cartItems':cartItems}
#         return render(request, 'ecommerce/checkout.html', context)

# def processOrder(request):
#         transaction_id = datetime.datetime.now().timestamp()
#         data = json.loads(request.body)

#         if request.user.is_authenticated:
#             client = request.user.client
#             order, created = Order.objects.get_or_create(client=client, complete=False)
#         else:
#             client, order = guestOrder(request, data)

#         total = float(data['form']['total'])
#         order.transaction_id = transaction_id

#         if total == order.get_cart_total:
#             order.complete = True
#         order.save()

#         if order.shipping == True:
#               ShippingAddress.objects.create(
#               client=client,
#               order=order,
#               address=data['shipping']['address'],
#               city=data['shipping']['city'],
#               state=data['shipping']['state'],
#               zipcode=data['shipping']['zipcode'],  
#               )

#         return JsonResponse('Payment submitted..', safe=False)


