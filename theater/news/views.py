from django.shortcuts import render

from main.models import CarouselleImage
from performances.models import Performance


def news(request):
    return render(request, 'news.html', locals())