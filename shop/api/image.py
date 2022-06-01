from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

from shop.services.images_service import ImageSaver
from django.views.decorators.csrf import csrf_exempt
from shop.services.json_service import json_response
from shop.services.request_service import BaseRequestEntity
from shop.services.error_service import ErrorException, FIELD_REQUIRED
from shop.models.image_model import ImageProductRelation
from shop.serializers import ImageSerializer
import json

@csrf_exempt
def upload_image(request):
    image_model = ImageSaver.process_image(request.FILES['img'])
    return HttpResponse(
        DjangoJSONEncoder(ensure_ascii=False).encode(ImageSerializer(image_model).data),
        content_type="application/json; encoding=utf-8",
        status=200,
    )

class ImageProductRelationtEntity(BaseRequestEntity):
    images = []
    product = None

    def verify(self):
        if self.product is None:
            raise ErrorException(FIELD_REQUIRED, 'Укажите параметр product')
        return self

@csrf_exempt
def upload_install_product(request):
    request_entity = ImageProductRelationtEntity(request.body).verify()
    ImageProductRelation.create(request_entity.images, request_entity.product)
    return HttpResponse(
        status=200,
    )




