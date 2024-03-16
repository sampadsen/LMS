from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import userdetails,bookdata


# Create your views here.
def home(request):
    return render(request,"homepage1.html")

def login(request):
    return render(request,"login.html")

def student(request):
        user_details=bookdata.objects.all()
        context={
            'b_details':user_details
        }
    
        return render(request,"student.html",context)

def issue(request):
    return render(request,"issue.html")

def returnbook(request):
    return render(request,"returnbook.html")

def register(request):
    if request.method== "POST":
        NAME=request.POST ['name']
        ID=request.POST['id']
        new=userdetails(name=NAME,id_1=ID)
        new.save()
    
    return render(request,'login.html')



def issued(request):
    if request.method== "POST":
        s_code=request.POST ['s_code']
        b_code=request.POST['b_code']
        i_date=request.POST['i_date']
        r_date=request.POST['r_date']
        

        new=bookdata(s_code=s_code,b_code=b_code,issue_date=i_date,return_date=r_date)
        new.save()
        return redirect('/student')
    
    return redirect('/student')
