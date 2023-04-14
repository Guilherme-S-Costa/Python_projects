from django.shortcuts import render

from .models import Order, OrderItem, Product

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'ecommerce/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        client = request.user.client
        order = Order.objects.filter(client_id=request.user.pk, completed_at__isnull=True).first()
        items = OrderItem.objects.filter(order_id=order.pk)
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0} 

    context = {'items': items, 'order': order}
    return render(request, 'ecommerce/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, completed_at=None)
        items = order.orderitem_set.all()
    else:
        items = []  
        order = {'get_cart_total':0, 'get_cart_item':0} 


    context = {'item': items, 'order':order}
    return render(request, 'ecommerce/checkout.html', context)

