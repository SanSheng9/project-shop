from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from secret_shop.settings import AUTH_USER_MODEL
from shop.models import Product


class Order(models.Model):
    address = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    sum = models.DecimalField(max_digits=7, decimal_places=2)
    anonymous = models.BooleanField(blank=True)
    username = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    first_lastname = models.CharField(max_length=255)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    checked = models.BooleanField(blank=False, default='False')


class OrderProductRelation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
