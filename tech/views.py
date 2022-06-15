from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from tech.forms import Login, Signup, adduser
from tech.models import Profile

# Create your views here.

def home(request):
    return render(request,"base.html")

def usersignup(request):
    if request.method == "POST":
        sp = Signup(request.POST)
        if sp.is_valid():
            sp.save()
    else:
        sp = Signup()
        return render(request,'signup.html',{'form':sp})

def userlogin(request):
    if request.method == "POST":
        lf = Login(request=request,data=request.POST)
        uname = lf.cleaned_data['username']
        upass = lf.cleaned_data['password']
        user = authenticate(username=uname,password=upass)
        if user is not None:
            login(request, user)
    else:
        lf = Login()
        return render(request,"login.html",{'fm':lf})

#create
def createuser(request):
    if request.method == "POST":
       fm = adduser(request.POST)
       if fm.is_valid():
        fm.save()
    else:
        fm = adduser()
        user = Profile.objects.all()
    return render(request,"adduser.html",{'form':fm , 'use':user})

#update
def update(request,id):
    if request.method == "POST":
        pi = Profile.objects.get(pk=id)
        fm = adduser(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Profile.objects.get(pk=id)
        fm = adduser(instance=pi)
    return render(request,'adduser.html',{'form':fm})

#delete
def delete_data(request, id):
    if request.method =="POST":
        pi = Profile.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')



