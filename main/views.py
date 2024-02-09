from django.shortcuts import render


def main(request):

    context = {
        'is_homepage': True
    }
    return render(request, 'main/main.html', context)

def other_page(request):
    return render(request, 'other_page.html', {'is_homepage': False})


def section1(request):

    return render(request, 'main/section1.html')

def section2(request):

    return render(request, 'main/section2.html')

def section3(request):

    return render(request, 'main/section3.html')

def section4(request):

    return render(request, 'main/section4.html')

def section5(request):

    return render(request, 'main/section5.html')


def section6(request):

    return render(request, 'main/section6.html')