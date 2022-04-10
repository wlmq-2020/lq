<<<<<<< HEAD
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
=======
from django.shortcuts import render
from datetime import datetime
# Create your views here.
>>>>>>> 46ec191bfa6bb9bc6036760695e0af898b8749d6


def timestr(request):
    time_str = datetime.now().strftime("%Y-%m-%d-%X")
<<<<<<< HEAD
    return render(request, 'index.html', {'now': time_str})


def articles(request, year, month):
    return HttpResponse(f'{year}-{month}')


def login(request):
    return render(request, 'login.html')

@csrf_exempt
def auth(request):
    print(request.POST)
    return redirect('/blog/times')
=======
    return render(request,'index.html',{'now':time_str})
>>>>>>> 46ec191bfa6bb9bc6036760695e0af898b8749d6
