from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *
# Create your views here.

def myView(request):
  return render_to_response('404.html')

def home(request):
    if request.method == 'POST':
        em = request.POST.get('em')
        Subscribe(em=em).save()
        return render(request,'home.html',{'data':'Subscribe Successfully....!'})
    blog = Blog.objects.all()[:6]
    service = Services.objects.all()[:3]
    return render(request,'home.html',{'blog':blog,'service':service})

def meet_choach(request):
    return render(request,'meet_choach.html')

def podcast(request):
    return render(request,'podcast.html')

def our_service(request):
    service = Services.objects.all()
    return render(request,'services.html',{'service':service})

def blog(request):
    blog = Blog.objects.all()
    return render(request,'blog.html',{'blog':blog})

def product(request):
    product = Products.objects.all()
    return render(request,'press.html',{'blog':product})

def program(request):
    program = Programs.objects.all()
    return render(request,'resources.html',{'blog':program})

def contact(request):
    if request.method == 'POST':
        nm = request.POST.get('nm')
        em = request.POST.get('em')
        no =request.POST.get('no')
        msg =request.POST.get('feed')
        Contact(name=nm,email=em,no=no,msg=msg).save()
        return render(request,'contact.html',{'data':'Sent Successfully....!'})
    return render(request,'contact.html')

def services_details(request,nm,id):
    service_details = Services.objects.all().filter(id=id)
    return render(request,'services_details.html',{'service_details':service_details})

def blog_details(request,title,id):
    blog_details = Blog.objects.all().filter(id=id)
    return render(request,'blog_details.html',{'blog_details':blog_details})
