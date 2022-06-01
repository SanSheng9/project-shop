
from django.db.models import Avg

from shop.models import UserProductRelation
from shop.models.order_model import OrderProductRelation


def set_rating(product):
    rating = UserProductRelation.objects.filter(product=product).aggregate(rating=Avg('rate')).get('rating')
    product.rating = rating
    product.save()

def createOrderProductRelationModel(product, order):
    for p in product:
        OrderProductRelation.objects.create(product=p, order=order)