from django.template import Library
from app import utils

register = Library()

@register.filter
def format_money(value):
    return utils.format_money(value)
  
@register.filter
def calculate_cart_items(cart: dict):
    return utils.calculate_quantity_cart(cart)

@register.filter
def calculate_cart_total_value(cart: dict):
    return utils.calculate_cart_total_value(cart)