from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from secret_shop import settings
from shop.models import Product, UserProductRelation, UserProfile, ImageObject
from shop.models.order_model import Order


class ImageSerializer(ModelSerializer):
    original = serializers.FilePathField(path=settings.MEDIA_ROOT)
    miniature = serializers.FilePathField(path=settings.MEDIA_ROOT)
    preview = serializers.FilePathField(path=settings.MEDIA_ROOT)
    original_width = serializers.IntegerField()
    original_height = serializers.IntegerField()
    miniature_width = serializers.IntegerField()
    miniature_height = serializers.IntegerField()
    preview_width = serializers.IntegerField()
    preview_height = serializers.IntegerField()

    class Meta:
        model = ImageObject
        fields = ('id', 'original', 'miniature', 'preview', 'original_width', 'original_height', 'miniature_width',
                  'miniature_height',
                  'preview_width', 'preview_height')


class ProductSerializer(ModelSerializer):
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)

    #    favourites = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'img', 'price', 'seller', 'rating')

    # def get_favourites(self, instance, request):
    #    obj = UserProductRelation.objects.values('favourites').filter(pk=instance.id, user=request.user)
    #    return obj


class UserSerializer(ModelSerializer):
    favourites = serializers.SerializerMethodField(read_only=True)
    bucket = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'avatar', 'is_superuser',
                  'favourites', 'bucket')

    def get_favourites(self, instance):
        return UserProductRelation.objects.values_list('product', flat=True).filter(user=instance.username,
                                                                                    favourites=True)

    def get_bucket(self, instance):
        return UserProductRelation.objects.values_list('product', flat=True).filter(user=instance.username,
                                                                                    bucket=True)


class UserProductRelationSerializer(ModelSerializer):
    class Meta:
        model = UserProductRelation
        fields = ('product', 'favourites', 'rate')


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'address', 'date', 'sum', 'anonymous', 'username', 'first_lastname', 'phone', 'check')


class OrderProduct(ModelSerializer):
    order = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

    def get_order(self, instance):
        return Order.objects.values_list('pk').filter(products=instance.id)