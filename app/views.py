from django.shortcuts import render
from datetime import datetime
# Create your views here.


def timestr(request):
    time_str = datetime.now().strftime("%Y-%m-%d-%X")
    return render(request,'index.html',{'now':time_str})