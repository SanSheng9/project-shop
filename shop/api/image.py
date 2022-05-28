from .utils import BaseRequestEntity
from shop.models.image_model import Image
from shop.services.error_service import ErrorException, FIELD_REQUIRED
from shop.services.images_service import ImageSaver
from django.views.decorators.csrf import csrf_exempt


class ImageEntity:
    original = ''
    miniature = ''
    preview = ''
    miniatureSizeWidth = 0
    miniatureSizeHeight = 0
    previewSizeWidth = 0
    previewSizeHeight = 0
    originalSizeWidth = 0
    originalSizeHeight = 0

    def __init__(self, image_model):
        self.id = image_model.id
        self.original = image_model.original
        self.miniature = image_model.miniature
        self.preview = image_model.preview
        self.originalSizeWidth = image_model.original_width
        self.originalSizeHeight = image_model.original_height
        self.miniatureSizeWidth = image_model.miniature_width
        self.miniatureSizeHeight = image_model.miniature_height
        self.previewSizeWidth = image_model.preview_width
        self.previewSizeHeight = image_model.preview_height


@csrf_exempt
def upload_image(request):
    image_model = ImageSaver.process_image(request.FILES['image'])
    return json_response(ImageEntity(image_model))




