from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse

from .models import News, Category, NewsImage, NewsVideo, NewsFile, Comment
from .forms import NewsForm, CommentForm, NewsImageForm, NewsVideoForm, NewsFileForm

import json
from random import sample


from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


def Publishers(request):

    categories = Category.objects.all()
    categories_news = {
        category.name: {
            'large_news': News.objects.filter(category=category).prefetch_related('images').order_by('-date_posted')[:1],
            'standard_news': News.objects.filter(category=category).prefetch_related('images').order_by('-date_posted')[1:4],
            'text_news': News.objects.filter(category=category).prefetch_related('images').order_by('-date_posted')[4:6],
        }
        for category in categories
    }

    context = {
        'categories': categories,
        'categories_news': categories_news,
    }

    return render(request, 'Publishers/Publishers.html', context)



def all_news(request):
    news_list = News.objects.all().order_by('-date_posted')  # Сортировка новостей от новых к старым
    paginator = Paginator(news_list, 10)  # Показывать по 5 новостей на странице

    categories = Category.objects.all()  # Получаем все категории из базы данных

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Publishers/page_all_news.html', {'page_obj': page_obj, 'categories': categories})


def news_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news_list = News.objects.filter(category=category).order_by('-date_posted')
    paginator = Paginator(news_list, 10)  # Укажите здесь нужное количество новостей на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Publishers/page_news_category.html', {
        'category': category,
        'page_obj': page_obj,
    })


@csrf_exempt
def page_news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    comments = news.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.news = news
                new_comment.author = request.user
                new_comment.save()

                # Создаем ответ для AJAX
                data = {
                    'status': 'ok',
                    'author': new_comment.author.username,
                    'content': new_comment.content,
                    'created_at': new_comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                }
                return JsonResponse(data)
            else:
                return JsonResponse({'status': 'error', 'errors': comment_form.errors}, status=400)
        else:
            # Обработка обычной формы POST
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.news = news
                new_comment.author = request.user
                new_comment.save()
                return redirect('page_news_detail', news_id=news_id)

    # Если нет пользовательской структуры, создаем пустой список блоков
    content_blocks = json.loads(news.content_structure) if news.content_structure else []

    # Получаем случайные новости, исключая текущую просматриваемую новость
    all_news_ids = News.objects.exclude(id=news_id).values_list('id', flat=True)
    random_ids = sample(list(all_news_ids), min(len(all_news_ids), 3))
    random_news = News.objects.filter(id__in=random_ids)

    context = {
        'news': news,
        'content_blocks': content_blocks,
        'comments': comments,
        'comment_form': comment_form,
        'random_news': random_news,
    }

    return render(request, 'Publishers/page_news_detail.html', context)


@csrf_exempt
@login_required
def create_news_view(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            # Обработка JSON данных
            data = json.loads(request.body)
            form = NewsForm(data)
            if form.is_valid():
                news_item = form.save(commit=False)
                news_item.author = request.user
                news_item.save()
                # Здесь можно добавить код для обработки множественных файлов, если это необходимо и возможно с JSON
                return JsonResponse({'status': 'success', 'news_id': news_item.id}, status=200)
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
        else:
            # Обработка данных формы с файлами
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():
                news_item = form.save(commit=False)
                news_item.author = request.user
                news_item.save()

                # Обработка загруженных изображений
                images = request.FILES.getlist('images')
                for image_file in images:
                    NewsImage.objects.create(news=news_item, image=image_file)

                # Обработка загруженных видео
                videos = request.FILES.getlist('video')
                for video_file in videos:
                    NewsVideo.objects.create(news=news_item, video=video_file)

                # Обработка загруженных файлов
                files = request.FILES.getlist('file')
                for file in files:
                    NewsFile.objects.create(news=news_item, file=file)

                return HttpResponseRedirect(reverse('page_news_detail', args=[news_item.id]))
    else:
        form = NewsForm()

    return render(request, 'Publishers/create_news.html', {'form': form})