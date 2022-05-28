from django.db import models
from shop.models.product_model import Product

class Image(models.Model):
    original = models.CharField(max_length=255)
    miniature = models.CharField(max_length=255)
    preview = models.CharField(max_length=255)
    original_width = models.IntegerField()
    original_height = models.IntegerField()
    miniature_width = models.IntegerField()
    miniature_height = models.IntegerField()
    preview_width = models.IntegerField()
    preview_height = models.IntegerField()

    @staticmethod
    def get_by_id(id):
        try:
            return Image.objects.get(pk=id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_all():
        return Image.objects.all().order_by("-id")

    @staticmethod
    def create(original, miniature, preview, original_width, original_height, miniature_width, miniature_height,
               preview_width, preview_height):
        return Image.objects.create(
            original=original, miniature=miniature, preview=preview,
            original_width=original_width, original_height=original_height,
            miniature_width=miniature_width, miniature_height=miniature_height,
            preview_width=preview_width, preview_height=preview_height
        )

class ImageRelation(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
