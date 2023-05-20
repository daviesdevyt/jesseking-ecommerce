from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib import messages
import os

# Create your views here.
@login_required
def edit_products_list(request):
    products = Product.objects.filter(in_draft=False).all()
    return render(request, "edit.html", {"products":products, "draft":False})

@login_required
def edit_products_draft(request):
    products = Product.objects.filter(in_draft=True).all()
    return render(request, "edit.html", {"products":products, "draft":True})

@login_required
def create_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        in_stock = True if request.POST.get("in_stock") else False
        in_draft = True if request.POST.get("in_draft") else False
        image = request.FILES.get('image')
        Product.objects.create(name=name, in_stock=in_stock, in_draft=in_draft, image=image)
    return redirect(request.META["HTTP_REFERER"])

@login_required
def edit_product(request):
    if request.method == "POST":
        _id = request.POST.get("id")
        name = request.POST.get("name")
        in_stock = True if request.POST.get("in_stock") else False
        in_draft = True if request.POST.get("in_draft") else False
        image = request.FILES.get('image')
        prod = Product.objects.get(id=_id)
        if prod:
            prod.name = name
            prod.in_draft = in_draft
            prod.in_stock = in_stock
            if image:
                os.remove(prod.image.path)
                prod.image = image
            prod.save()
    return redirect(request.META["HTTP_REFERER"])

@login_required
def delete_product(request):
    if request.method == "POST":
        _id = request.POST.get("id")
        prod = Product.objects.get(id=_id)
        if prod:
            try:
                os.remove(prod.image.path)
            except:
                pass
            prod.delete()
    return redirect(request.META["HTTP_REFERER"])


def login_page(request):
    if request.method == "POST":
        pwd = request.POST.get("password")
        user = authenticate(request, username="jesseking", password=pwd)
        if user:
            login(request, user)
            return redirect("edit_products_list")
        else:
            messages.error(request, "Incorrect password")
            return redirect('login')
    return render(request,"login.html")

@login_required
def logout_user(request):
    logout(request)
    return redirect("login")