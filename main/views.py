from django.shortcuts import render, get_object_or_404
from Publishers.models import News
from .models import Slide



def main(request):

    latest_news = News.objects.all().prefetch_related('images').order_by('-date_posted')[:2]
    slides = Slide.objects.all().order_by('order')  # Получаем все слайды, отсортированные по полю order
    context = {
        'latest_news': latest_news,
        'slides': slides,  # Добавляем слайды в контекст
        'is_homepage': True,
    }

    return render(request, 'main/main.html', context)


def other_page(request):

    return render(request, 'other_page.html', {'is_homepage': False})


def section1(request):

    latest_news = News.objects.all().prefetch_related('images').order_by('-date_posted')[:2]
    slides = Slide.objects.all().order_by('order')  # Получаем все слайды, отсортированные по полю order
    context = {
        'latest_news': latest_news,
        'slides': slides,  # Добавляем слайды в контекст
        'is_homepage': True,
    }

    return render(request, 'main/section1.html', context)

def section2(request):

    latest_news = News.objects.all().prefetch_related('images').order_by('-date_posted')[:5]
    context = {
        'latest_news': latest_news,
    }
    return render(request, 'main/section2.html', context)


def section3(request):

    return render(request, 'main/section3.html')

def section4(request):

    return render(request, 'main/section4.html')

def section5(request):

    return render(request, 'main/section5.html')


def section6(request):

    return render(request, 'main/section6.html')

def in_vork(request):

    return render(request, 'main/in_vork.html')

