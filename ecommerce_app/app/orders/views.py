from django.views.generic.detail import DetailView
from django.views import View
from .models import Order
from django.views.generic.list import ListView


class DispatchLoginRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return super().get_queryset()
    

class OrdersList(DispatchLoginRequiredMixin, ListView):
    model = 'Order'
    context_object_name = 'orders'
    template_name = 'list_order.html'
    paginate_by = 10
    ordering = ['-id']


class OrderDetailView(DispatchLoginRequiredMixin, DetailView):
    model = Order
    context_object_name = 'orders'
    template_name = 'detail_order.html'
    pk_url_kwarg = 'pk'

class CloseOrderView(View):
    pass

class PayOrderiew(DispatchLoginRequiredMixin, DetailView):
    model = Order
    context_object_name = 'orders'
    template_name = 'pay_order.html'
    pk_url_kwarg = 'pk'
