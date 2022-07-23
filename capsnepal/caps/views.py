import re
from django.shortcuts import redirect, render,HttpResponse
from caps.models import Cap

# Create your views here.
def index(request):
    caps = Cap.objects.all()
    return render(request, 'caps.html', {'data':caps})

def about(request):
    return render(request, 'about.html', {})


def login(request):
    return render(request,'login.html',{})

def register(request):
    return render(request,'register.html',{})

def show_create_caps(request):
    return render(request,'create_caps.html',{})

def most_viewed(request):
    return render(request,'most_viewed.html',{})

def best_seller(request):
    return render(request,'best_seller.html',{})

def latest_arrivals(request):
    return render(request,'latest_arrivals.html',{})

def custom_caps(request):
    return render(request,'custom_caps.html',{})

def create_caps(request):
    if request.method=="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        get_pictures = request.FILES.get('file')
        model = Cap(name=name, image=get_pictures, desc=description,
            price=price)
        model.save()
        return render(request, 'create_caps.html', {'message':"data is stored successfully"})
    
    return render(request,'create_caps.html', {'message':'problem storing the data'})



def show_caps(request,id=None):
    if request.method=="GET":
        if id:
            cap = Cap.objects.get(id=id)
            return render(request, 'show_caps.html', {'data':cap})
        caps = Cap.objects.all()
        return render(request, 'show_caps.html', {'data':caps})
    return render(request,'create_caps.html', {'message':'problem fetching the data'})


def show_cap_details(request, id):
    cap = Cap.objects.get(id=id)

    return render(request, "update_cap.html", {'cap':cap})