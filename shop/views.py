from django.shortcuts import render
from .models import Product, Orders
from math import ceil
from django.http import HttpResponse
# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides), 'product':products}

    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats : 
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1,nSlides), nSlides])
    # allprods = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    params = {'allprods':allprods}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        print(name)
    return render(request, 'shop/contact.html')   

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')        

def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        zipCode = request.POST.get('zip','')
        state = request.POST.get('state','')
        city = request.POST.get('city','')
        Order = Orders(name=name, email=email, zipCode = zipCode, state=state, city=city)
        Order.save()
    return render(request, 'shop/checkout.html') 

def products(request, myid):
    product = Product.objects.filter(id=myid)
    # print(product)
    return render(request, 'shop/productview.html', {'product':product[0]})