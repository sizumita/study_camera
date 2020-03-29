from django.core.management.base import BaseCommand
from camera.models import Image
import cv2
from PIL import Image as PImage
import io
from django.core.files.base import ContentFile


class Command(BaseCommand):

    def handle(self, *args, **options):
        c = cv2.VideoCapture(0)
        c.read()
        r, img = c.read()
        cv2.imwrite('test.jpg', img)
        c.release()
        buffer = io.BytesIO()
        image = PImage.fromarray(img)
        image.save(buffer, format='JPEG')
        image = Image(name='sizumita')
        image.save()
        image.picture.save(image.picture.name, ContentFile(buffer.getvalue()))
        buffer.close()
