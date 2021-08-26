from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    ak = newu.objects.all()
    return render(request,"app/home.html",{'ni':ak})

def newr(request):
    return render(request, "app/Edit-user.html")

def editu(request,pk):
    ad = newu.objects.get(id=pk)
    print(f"-----------------------------------------------------------------------------------{ad}")
    return render(request,"app/test.html",{'as': ad})

def user(request):
    if request.method == 'POST':
        Fn = request.POST['fn']
        Un = request.POST['username']
        em = request.POST['email']
        im = request.FILES['Img']

        usernew = newu.objects.create(
            fname = Fn,
            uname = Un,
            email = em,
            img = im 
        )     
        return redirect("home")
    else:
        return redirect('newr')


def delete(request,pk):
    delus = newu.objects.get(id=pk)
    print(f"-----{delus}-----")
    delus.delete()
    return redirect("home")

def update_user(request):
    if request.method == POST:
        upd = newu.objects.get(id=pk)

        upd.fname = request.POST['name'] if request.POST['name'] else upd.fname
        upd.uname = request.POST['username'] if request.POST['username'] else upd.uname
        upd.save()
    
    return redirect('home')