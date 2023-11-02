from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product

def homepage(request):
   all_products = Product.objects.all()
   context = {"all_products": all_products}
   # return HttpResponse("<h1>Welcome to Konga</h1>")
   return render(request, "store/index.html", context)
   # return render(request, response)

def detailpage(request, input_id):
   current_product = Product.objects.get(id=input_id)
   context = {"current_product": current_product}
   return render(request, "store/detail.html", context) 


def createproductpage(request):
    if request.method == "POST":
      form = ProductForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("/")
      else:
       return HttpResponse("Something went wrong")
    else:
     form = ProductForm()
    context = {"form": form}
    return render(request, "store/create_product.html", context)
        

# Create your views here.
