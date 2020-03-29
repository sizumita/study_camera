from django.db import models
from django.utils import timezone
# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=100)
    when = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='images/')