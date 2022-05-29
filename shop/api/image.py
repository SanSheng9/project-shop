from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

from shop.services.images_service import ImageSaver
from django.views.decorators.csrf import csrf_exempt
from shop.services.json_service import json_response
from shop.serializers import ImageSerializer

@csrf_exempt
def upload_image(request):
    image_model = ImageSaver.process_image(request.FILES['img'])
    return HttpResponse(
        DjangoJSONEncoder(ensure_ascii=False).encode(ImageSerializer(image_model).data),
        content_type="application/json; encoding=utf-8",
        status=200,
    )




