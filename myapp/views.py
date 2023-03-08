from django.shortcuts import render
from .models import Contactus
# Create your views here.

def index(request):
    return render(request,'myapp/index.html')


def about(request):
    return render(request, 'myapp/about.html')


def project(request):
    return render(request, 'myapp/project.html')
    
def contactus(request):
    thank = False
    message =  False
    if request.method=="POST":
        
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        name = fname+" " +lname
        message = request.POST.get('message', '')
        contact = Contactus(fname=fname,lname=lname,name=name, email=email, message=message)
        contact.save()
        message = f"Thank you for contacting us {fname}! We will reach out to you soon."
        thank = True
        text = True
    return render(request, 'myapp/contactus.html', {'message':message })
