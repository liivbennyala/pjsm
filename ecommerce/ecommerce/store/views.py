from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def store(request):
    return render(request,'store.html')
def checkout(request):
    return render(request, 'checkout.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request, 'index.html')
def product(request):
    return render(request, 'product.html')
def services(request):
    return render(request, 'service.html')
def single(request):
    return render(request, 'single.html')