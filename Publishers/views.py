from django.shortcuts import render

def Publishers(request):

    return render(request, 'Publishers/Publishers.html')


def page_all_news(request):

    return render(request, 'Publishers/page_all_news.html')


def news(request):

    return render(request, 'Publishers/news.html')