from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contactus
from home.models import Order
from django.contrib import messages

# Create your views here.

def index1(request):
    context={
        'variable':"this is sent"
    }
    return render(request,'demo.html',context)

def about(request):
    return HttpResponse('<h1 style="color:green;">This is about page</h1>')
    
def server(request):
    return HttpResponse('<h1 style="color:red;">This is server page</h1>')
    
def contact(request):
    return HttpResponse('<h1 style="color:blue;">This is contact page</h1>')
    
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def order(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        choices=request.POST.get('choices')
        quantity=request.POST.get('quantity')
        desc=request.POST.get('desc')
        address=request.POST.get('address')
        order = Order(name=name, email=email, phone=phone, option=choices, quantity=quantity, desc=desc, address=address, date=datetime.now())
        order.save()
        messages.success(request, "Order has been place .Thank u !")
        
    return render(request,'order.html')


# def contactus(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         desc = request.POST.get('desc')
#         contact_model = Contactus(name=name, email=email, phone=phone, desc=desc)
#         contact_model.save()
#         messages.success(request, "ur message has been sent.")

#     return render(request, 'contactus.html')


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contactus(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, "Your message has been sent!!")

    return render(request, 'contactus.html')

def gallery(request):
    return render(request,'gallery.html')

