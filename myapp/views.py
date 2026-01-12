from django.shortcuts import render
from myapp.models import Skills,Profile,Project

# Create your views here.



def index(request):
    
    pro=Profile.objects.all()
    data={
        "pro":pro
    }
    return render(request,"index.html",data)



def ABOUT(request):
    pro_1=Profile.objects.all()
    data={
        "pro_1":pro_1
    }
    return render(request,"ABOUT.html",data)



