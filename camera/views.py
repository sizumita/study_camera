from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Image


def showall(request):
    images = Image.objects.all()[::-1][:1000]
    context = {'images': images
               }
    return render(request, 'index.html', context)
