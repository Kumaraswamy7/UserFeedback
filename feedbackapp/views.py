from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserData,UsrFeed



# Create your views here.


def index(request):
    return render(request, 'index.html')
def index2(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')

def feedback(request):
    if request.method == 'POST':
        name=request.POST.get('usrname')
        password=request.POST.get('password')
        if UserData.objects.filter(usrname=name).exists():
            user=UserData.objects.get(usrname=name)  
            if user.password==password:
                request.session['name'] =user.usrname
                request.session['id'] =1
                return render(request,'feedback.html',{'name':user.usrname})
            else:
                return render(request,'login.html',{'password_wrong':True})
        elif UserData.objects.filter(email=name).exists():
            user=UserData.objects.get(email=name)  
            if user.password==password:
                request.session['name'] =user.usrname
                request.session['email'] =name
                request.session['idt'] =2
                return render(request,'feedback.html',{'name':user.usrname})
            else:
                return render(request,'login.html',{'password_wrong':True})
        else:
            return render(request,'login.html',{'username or email wrong':True})

def home(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        
        if password1 == password2:
            if UserData.objects.filter(usrname=name).exists():
                return render(request,'register.html',{'name_exists':True})
            elif UserData.objects.filter(email=email).exists():
                return render(request,'register.html',{'email_exists':True})
            else:
                obj1=UserData(usrname=name,email=email,password=password1)
                request.session['name'] = obj1.usrname
                obj1.save()
                return redirect('/')
        else:
            return render(request,'register.html',{'password_not_match':True})
        




def thanku(request):
    name=request.session.get('name')
    email=request.session.get('email')
    idt=request.session.get('idt')
    if idt==1:
        obj=UserData.objects.get(usrname=name)
        name=obj.usrname
    elif idt==2:
        obj=UserData.objects.get(email=email)
        name=obj.email

    # elif id == 2:
    #     email=request.session.get('email')
    #     obj=UserData.objects.get(email=email)  
    
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        suggestion=request.POST.get('suggestion')
        if idt==1:
            UserData.objects.filter(usrname=name).update(feedback=feedback, suggestion=suggestion)
        if idt==2:
            UserData.objects.filter(email=name).update(feedback=feedback, suggestion=suggestion)
        
        
        # obj=UserData(feedback=feedback,suggestion=suggestion)
        # obj.save()
        

        return render(request, 'thanku.html',{'name':name})




