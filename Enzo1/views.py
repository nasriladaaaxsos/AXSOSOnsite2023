from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def index(request):
    return render(request, "index.html")


#Since this method wil recive the data of post request that it must end with redirect 
def Registration(request):
    fname = request.POST['fname']
    Sname = request.POST['sname']
    Tele = request.POST['telephone']
    Email = request.POST['email']

    #CRUD
    #Create
    User.objects.create(FirstName = fname, SecondName = Sname, Tele = Tele , Email = Email)

    #Update 
    # Userdata = User.objects.get(id = 1)
    # Userdata.Email = "Hakim_Bara@gmail.com"
    # Userdata.save()

    return redirect("/")  # Route 

def get_all_users(request):
    context = {
        "Allusers" : User.objects.all()
    }
    return render(request, "Allusers.html",context)


def delete_user(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect("/All")


def edituser(request, id):
    context = {
        "User" :   User.objects.get(id = id)
    }
    return render(request,"edituser.html" , context)

def editpost(request):
    fname = request.POST['fname']
    Sname = request.POST['sname']
    Tele = request.POST['telephone']
    Email = request.POST['email']
    id = request.POST["userid"]

    Userdata = User.objects.get(id = id )
    Userdata.Email = Email
    Userdata.SecondName = Sname
    Userdata.Tele = Tele
    Userdata.FirstName = fname
    Userdata.save()

    return redirect("/All")