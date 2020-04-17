from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("from about")

def contact(request):
    return HttpResponse("from contact")   

def tracker(request):
    return HttpResponse("from tracker")

def search(request):
    return HttpResponse("from product view")        

def checkout(request):
    return HttpResponse("from search") 

def productview(request):
    return HttpResponse("from product view")