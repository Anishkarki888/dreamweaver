from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import userForms
from service.models import Service

def homepage(request):
    servicesData= Service.objects.all()
    for a in servicesData:
        print(a.service_icon)
    
    data={
        'serviceData':servicesData
    }
    return render(request,"index.html")


def education(request):
    return render(request,"education.html")


def employment(request):
    return render(request,"employment.html")


def apply(request):
    finalans=0
    data={}
    try:
        if request.method=="post":
            
            name=str(request.POST.get['name'])
            reason=str(request.POST.get['reason'])
            email=str(request.POST.get['email'])
            phone=int(request.POST.get['phone'])
            finalans=name+reason+email+phone;
            data={
                'name':name,
                'reason':reason,
                'email':email,
                'phone':phone,
                'output':finalans
            }
            url="employment/?output={}".format(finalans)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"apply.html",data)

def course(request):
    return render(request,"course.html")

def signup(request):
    context = {}

    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if User.objects.filter(username=uname).exists():
            context['error'] = "Username already exists"
        
        elif pass1 != pass2:
            return HttpResponse("Passwords do not match")
        
        else:
        
            myuser = User.objects.create_user(uname, email, pass1)
            myuser.save()
            return redirect('login')
    
    return render(request, 'signup.html')
        
   

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('updates')
        else:
            return HttpResponse("username or password is incorrect!!!")
    return render(request,"login.html")


def submitform(request):
    try:
        if request.method=="post":
            name=str(request.POST.get['name'])
            reason=str(request.POST.get['reason'])
            email=str(request.POST.get['email'])
            phone=int(request.POST.get['phone'])
            finalans=name+reason+email+phone;
            data={
                'name':name,
                'reason':reason,
                'email':email,
                'phone':phone,
                'output':finalans
            }

      
            return HttpResponse(request)
    except:
        pass

def usersForms(request):
    finalans=0
    fn=userForms()
    data={'form':fn}
    try:
        if request.method=="post":
            name=str(request.POST.get('name'))
            reason=str(request.POST.get('reason'))
            email=str(request.POST.get('email'))
            phone=str(request.POST.get('phone'))
            finalans=name+reason+email+phone;
            data={
               'form':fn,
               'output':finalans
            }
            url="/employment/?output={}".format(finalans)

            return redirect(url)
    except:
            pass
    return render(request,"userform.html",data)

      

def usa(request):
    return render(request,"usa.html")

def updates(request):
    return render(request,"updates.html")

def loggedin(request):
    return render(request,"loggedin.html")


def working(request):
    return render(request,"future.html")
# def courses(request):
#     return HttpResponse("coursepage")

# def coursesDetails(request,courseid):
#     return HttpResponse(courseid)