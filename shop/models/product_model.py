from django.db import models
from secret_shop.settings import AUTH_USER_MODEL

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    img = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='default.svg')
    seller = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='my_products')
    shoppers = models.ManyToManyField(AUTH_USER_MODEL, through='UserProductRelation', related_name='products')
    count = models.PositiveSmallIntegerField(blank=False, default=1)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=None, null=True)

    def __str__(self):
        return f'ID {self.id}: {self.name}'