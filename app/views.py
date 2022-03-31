from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def timestr(request):
    time_str = datetime.now().strftime("%Y-%m-%d-%X")
    return render(request, 'index.html', {'now': time_str})


def articles(request, year, month):
    return HttpResponse(f'{year}-{month}')


def login(request):
    return render(request, 'login.html')

@csrf_exempt
def auth(request):
    print(request.POST)
    return redirect('/blog/times')