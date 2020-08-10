from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trail(request):
    return HttpResponse("<h1> project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="sachin"
    return render(request,"myapp/profile.html",{'name':name})

def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})

def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse("<h1>thanks for submitting mr./ms. {}</h1>".format(name))
    return render(request,"post_demo.html")
    
            



