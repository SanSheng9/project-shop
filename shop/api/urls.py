from django.urls import include, path
from .image import upload_image

urlpatterns = [
    path("image/upload", upload_image),
]