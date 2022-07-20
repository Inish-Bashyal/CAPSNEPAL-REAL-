import re
from django.shortcuts import render,HttpResponse
from caps.models import Cap

# Create your views here.
def index(request):
    caps = Cap.objects.all()
    return render(request, 'caps.html', {'caps':caps})

def about(request):
    return render(request, 'caps.html', {})


def login(request):
    return render(request,'capsnepal/caps/templates/login.html',{})