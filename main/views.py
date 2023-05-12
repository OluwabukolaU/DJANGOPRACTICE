from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render (request,"index.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        passowrd = request.POST["passowrd"]
        print(f"username:{username}")
        print(f"password:{password}")
        HttpResponseRedirect("/")

            
    return render (request,"login.html")


def register(request):
    return render (request,"register.html")



