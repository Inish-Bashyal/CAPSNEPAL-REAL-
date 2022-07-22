from base64 import encode
from django.shortcuts import redirect, render
from caps.models import Cap
from users.models import CustomUser
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register_name(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser(first_name=first_name, last_name=last_name,username=username, gender=gender, phone_number=phone_number,email=email,password=password)
        user.set_password(password)

        user.save()
        return render(request,'login.html',{'message':'user created successfully'})
    return render(request,'register.html',{'message':'method not allowed'})



def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['id'] = CustomUser.objects.get(username=username).id
            request.session['username'] = username

            if request.user.is_authenticated:
                caps = Cap.objects.all()
                return render(request, 'show_caps.html', {'data':caps})

        else:
            return render(request,'login.html',{'message':'credentials mismatched'})
    else:
        return render(request, 'login.html')


            


    


        
