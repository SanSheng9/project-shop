from django.urls import include, path
from .image import upload_image, upload_install_product

urlpatterns = [
    path("image/upload", upload_image),
    path("image/install/product", upload_install_product),
]