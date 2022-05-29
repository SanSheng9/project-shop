import uuid
from io import BytesIO

from PIL import Image

from shop.models.image_model import ImageObject


class ImageSaver:

    block_blob_service = None

    @staticmethod
    def save_image_to_storage(bucket, image_stream, image_name):
        bucket.put_object(
            Key=image_name,
            Body=image_stream,
            ACL='public-read',
            ContentType='image/jpeg',
        )

    @staticmethod
    def save_passport_to_local_storage(user_id, image_bytes, image_name):
        filename = "passports/{}_{}.jpg".format(user_id, image_name)
        im = Image.open(image_bytes)
        im.save(filename, 'JPEG')
        return filename

    @staticmethod
    def process_image(image):
        original = Image.open(image)
        format = ''

        if original.format == "PNG":
            format = '.png'
        else:
            format = '.jpg'

        # if original.mode in ("RGBA", "P"):
        #     original = original.convert("RGB")

        miniature = ImageSaver.resize_crop_image(original, (300, 300))
        preview = ImageSaver.resize_crop_image(original, (128, 128))

        original_name = str(uuid.uuid4()) + format
        original_bytes = BytesIO()
        original.save('media/'+original_name, format=original.format, optimize=True, quality=90) #progressive=True, 'JPEG'
        original_bytes.seek(0)

        miniature_name = str(uuid.uuid4()) + format
        miniature_bytes = BytesIO()
        miniature.save('media/'+miniature_name, format=original.format, quality=90)
        miniature_bytes.seek(0)

        preview_name = str(uuid.uuid4()) + format
        preview_bytes = BytesIO()
        preview.save('media/'+preview_name, format=original.format, quality=90)
        preview_bytes.seek(0)
        return ImageObject.create(
            original_name, miniature_name, preview_name,
            original.size[0], original.size[1],
            miniature.size[0], miniature.size[1],
            preview.size[0], preview.size[1],
        )

    @staticmethod
    def process_passport(executor, image_file):
        image = Image.open(image_file)

        filename = "passports/{}_{}.jpg".format(executor.id, str(uuid.uuid4()))
        image.save(filename, format='JPEG', quality=90)

        passport = model.users_model.Passport.create(
            filename, image.size[0], image.size[1]
        )
        executor.executor_passport = passport
        executor.save()

    @staticmethod
    def resize_crop_image(image, size):
        width = image.size[0]
        height = image.size[1]

        aspect = width / float(height)

        ideal_width = size[0]
        ideal_height = size[1]

        ideal_aspect = ideal_width / float(ideal_height)

        if aspect > ideal_aspect:
            # Then crop the left and right edges:
            new_width = int(ideal_aspect * height)
            offset = (width - new_width) / 2
            resize = (int(offset), int(0), int(width - offset), int(height))
        else:
            # ... crop the top and bottom:
            new_height = int(width / ideal_aspect)
            offset = (height - new_height) / 2
            resize = (int(0), int(offset), int(width), int(height - offset))

        return image.crop(resize).resize((int(ideal_width), int(ideal_height)), Image.ANTIALIAS)
