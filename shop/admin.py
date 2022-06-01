from django.contrib import admin
from django.contrib.admin import ModelAdmin

from shop.models import Product, UserProductRelation, UserProfile, ImageObject
from shop.models.order_model import Order

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass

@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    pass

@admin.register(UserProductRelation)
class UserProductRelationAdmin(ModelAdmin):
    pass

@admin.register(ImageObject)
class ImageObjectAdmin(ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass

