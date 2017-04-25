from django.shortcuts import render


def index(request):
    return render(request, 'person/home.html')


def contact(request):
    return render(request, 'person/basic.html',
                  {'content': ['If you would like to contact me, please email me.', 'email@gmail.com']})
