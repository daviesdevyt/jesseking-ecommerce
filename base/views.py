from django.shortcuts import render
from editor.models import Product

# Create your views here.
def home(request):
    products = Product.objects.filter(in_draft=False).all()
    return render(request, "index.html", {"products": products})

def about(request):
    return render(request, "about.html")