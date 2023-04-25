from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from .models import Product, Variation
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from pprint import pprint

class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 1
    
class ProductRetriveView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'

class AddCartView(View):
    def get(self, *args, **kwargs):
        http_refer = self.request.META.get('HTTP_REFERER', reverse('products:list'))
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            messages.error(self.request, 'Produto não existente')
            return redirect(http_refer)
        
        product_variation = get_object_or_404(Variation, pk=variation_id)
        product = product_variation.product

        if product_variation.stock < 1:
            messages.error(self.request, 'EStoque insuficiente')
            return redirect(http_refer)
        
        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()
        
        cart = self.request.session.get('cart')
        if variation_id in cart:
            qtd_product_in_cart = cart[variation_id]['quantity']
            qtd_product_in_cart += 1

            if product_variation.stock < qtd_product_in_cart:
                messages.error(self.request, f"Estoque insuficiente para {qtd_product_in_cart}, no produto {product.name}. Adicionamos {product_variation.stock} no  seu carrinho")
                qtd_product_in_cart = product_variation.stock

            cart[variation_id]['quantity'] = qtd_product_in_cart
            cart[variation_id]['unit_amount'] = float(product.amount * qtd_product_in_cart)
            cart[variation_id]['unit_promotional_amount'] = float(product.promotional_amount * qtd_product_in_cart)

        else:
            cart[variation_id] = {
                'product_id': product.pk,
                'product_name': product.name,
                'variation_name': product_variation.name,
                'variation_id': product_variation.pk,
                'unit_amount': float(product.amount),
                'unit_promotional_amount': float(product.promotional_amount),
                'quantity': 1,
                'slug': product.slug,
                'image': product.image.name or '',
            }

        self.request.session.save()
        messages.success(self.request, f"Produto {product.name} {product_variation.name} adicionado com sucesso ao carrinho.")
        return redirect(http_refer)


class RemoveFromCartView(View):
    def get(self, *args, **kwargs):
        http_refer = self.request.META.get('HTTP_REFERER', reverse('products:list'))
        variation_id = str(kwargs.get('id'))

        if not variation_id or not self.request.session.get('cart') or variation_id not in self.request.session['cart']:
            messages.error(self.request, 'Produto não existente')
            return redirect(http_refer)

        cart = self.request.session.get('cart')
        messages.success(self.request, f"Produto {cart[variation_id].get('product_name')} {cart[variation_id].get('variation_name')} removido do carrinho.")
        

        del cart[variation_id]
        self.request.session.save()
        return redirect(http_refer)

class CartView(View):
    def get(self, *args, **kwargs):
        url_redirect = 'products:finalize' if self.request.user.is_authenticated else 'accounts:list' 
        return render(self.request, 'products/cart.html', context={'btn_url_redirect': url_redirect})

class FinalizeCartView(View):

    
    def get(self, *args, **kwargs):

        if not self.request.user.is_authenticated:
            return redirect('accounts:list')
    
        context = {'user': self.request.user, 'cart': self.request.session.get('cart')}
        return render(self.request, 'products/resume.html', context)
