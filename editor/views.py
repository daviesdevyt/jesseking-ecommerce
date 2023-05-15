from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def edit_products_list(request):
    products = Product.objects.filter(in_draft=False).all()
    return render(request, "edit.html", {"products":products})

def create_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        in_stock = True if request.POST.get("in_stock") else False
        in_draft = True if request.POST.get("in_draft") else False
        Product.objects.create(name=name, in_stock=in_stock, in_draft=in_draft)
    return redirect("edit_products_list")

def edit_product(request):
    if request.method == "POST":
        _id = request.POST.get("id")
        name = request.POST.get("name")
        in_stock = True if request.POST.get("in_stock") else False
        in_draft = True if request.POST.get("in_draft") else False
        prod = Product.objects.get(id=_id)
        if prod:
            prod.name = name
            prod.in_draft = in_draft
            prod.in_stock = in_stock
            prod.save()
    return redirect("edit_products_list")

def delete_product(request):
    if request.method == "POST":
        _id = request.POST.get("id")
        prod = Product.objects.get(id=_id)
        if prod:
            prod.delete()
    return redirect("edit_products_list")
