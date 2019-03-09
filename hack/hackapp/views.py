from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as lg, logout
from .models import details
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'hackapp/page1.html')
    
# t=Tablee.objects.all()
# return render(request,'',t_var:"t")
def login(request):
    if request.method == 'POST':
        mail = request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(username=mail, password=pw)
        if user is not None:
            lg(request,user)
            return HttpResponse('shiva')
        else:
            #return redirect(reverse('index'))
            return render(request,'hackapp/page1.html') 
def page2(request):
    if request.method == 'POST':
        un=request.POST['username']
        eid=request.POST['emailid']
        pw=request.POST['password']
        bg=request.POST['bloodgroup']
        pn=request.POST['phonenumber']
        add=request.POST['address']
        city=request.POST['city']

        user=User.objects.create_user(username=un,email=eid,password=pw)
        user.is_staff=True
        user.save()

        det=details(blood_group=bg,contact=pn,add=add,city=city,user=user)
        det.save()

        return render(request,'hackapp/page1.html')
    else:
        return render(request,'hackapp/page1.html')

def whos(request):
    return render(request,'hackapp/page2.html')

def don(request):
    return render(request,'hackapp/page3d.html')

def req(request):
    return render(request,'hackapp/page3r.html')