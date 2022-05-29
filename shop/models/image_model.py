from django.db import models
from shop.models.product_model import Product

class ImageObject(models.Model):
    img_original = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='default.svg')
    img_miniature = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='default.svg')
    img_preview = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='default.svg')
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
            return ImageObject.objects.get(pk=id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_all():
        return ImageObject.objects.all().order_by("-id")

    @staticmethod
    def create(original, miniature, preview, original_width, original_height, miniature_width, miniature_height,
               preview_width, preview_height):
        return ImageObject.objects.create(
            img_original=original, img_miniature=miniature, img_preview=preview,
            original=original, miniature=miniature, preview=preview,
            original_width=original_width, original_height=original_height,
            miniature_width=miniature_width, miniature_height=miniature_height,
            preview_width=preview_width, preview_height=preview_height
        )

class ImageRelation(models.Model):
    image = models.ForeignKey(ImageObject, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
