from math import prod
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def home(request):
    form = HomeQuery()
    categories = Category.objects.all()
    products = {}

    for i in categories:
        if Product.objects.filter(category=i).count() > 0:
            products[i.category_name] = Product.objects.filter(category=i)

    context = {'categories': categories, 'products': products, 'form': form}

    if request.method == "POST":
        form = HomeQuery(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "home.html", context)

    return render(request, "home.html", context)


def contact_us(request):
    form = QueryForm()
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
        form = QueryForm()
        message = 'We will get in touch with you!!'
        return render(request, "contactus.html", {'form': form, 'message': message})

    return render(request, "contactus.html", {'form': form})


def product_page(request):
    categories = Category.objects.all()
    products = {}

    for i in categories:
        if Product.objects.filter(category=i).count() > 0:
            products[i.category_name] = Product.objects.filter(category=i)

    context = {'categories': categories, 'products': products}
    return render(request, "productpage.html", context)


def product_details(request, product_name):
    details = Product.objects.get(product_name=product_name)
    return render(request, "productdetails.html", {'details': details})


def category_specific(request, category_name):
    details = Category.objects.get(category_name=category_name)
    products = Product.objects.filter(category=details)
    return render(request, "categoryspecific.html", {'details': details, 'products': products})
