from django.shortcuts import render

from main.models import CarouselleImage
from performances.models import Performance
from news.models import Post


def main(request):
    firstCarouselleImage = CarouselleImage.objects.filter(firstField=True)
    carouselleImages = CarouselleImage.objects.filter(firstField=False)
    performances = Performance.objects.order_by('dateTime')
    posts = Post.objects.order_by()
    return render(request, 'main.html', locals())