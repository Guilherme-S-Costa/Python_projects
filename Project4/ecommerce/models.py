from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(verbose_name='preço', max_digits=5, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name 
    
    @property
    def imagensURL(self):
        try:
                url = self.imagens.url
        except: 
                url = ''
        return url


class Order(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    client_email = models.CharField(max_length=100, null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.pk} | {self.client_email}"

    @property
    def get_cart_total(self):
        sum = 0
        for item in self.items:
            sum += item.get_total
        return float(sum)
    
    @property
    def items(self):
        return OrderItem.objects.filter(order=self)
    
    @property
    def total_items(self):
        return self.items.count()
    
class OrderItem(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    product_value = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    product_add_at = models.DateTimeField(null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pk} | {self.client_id} | {self.product.name}"

    @property
    def get_total(self):
        return self.product_value

class ShippingAddress(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) 
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField()
                              
    def __str__(self):
        return self.address