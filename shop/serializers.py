from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from shop.models import Product, UserProductRelation, UserProfile, ImageObject


class ImageSerializer(ModelSerializer):
    original = serializers.FilePathField('/media')
    miniature = serializers.FilePathField('/media')
    preview = serializers.FilePathField('/media')
    original_width = serializers.IntegerField()
    original_height = serializers.IntegerField()
    miniature_width = serializers.IntegerField()
    miniature_height = serializers.IntegerField()
    preview_width = serializers.IntegerField()
    preview_height = serializers.IntegerField()
    class Meta:
        model = ImageObject
        fields = ('id','original', 'miniature', 'preview', 'original_width', 'original_height', 'miniature_width', 'miniature_height',
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
