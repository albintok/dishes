from email.mime import image
from unicodedata import category
from django.shortcuts import render,redirect
from django.views.generic import View
from api.models import Dishes

# Create your views here.

# localhost:8000/dishs/
class DishView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"dish.html")
    
    def post(self,request,*args,**kwargs):
        dname=request.POST.get("name")
        dcat=request.POST.get("cat")
        dprice=request.POST.get("price")
        dimage=request.POST.get("img")
        drating=request.POST.get("rate")
        Dishes.objects.create(name=dname,catagory=dcat,image=dimage,price=dprice,rating=drating)
        return render(request,"dish.html")

class DishlistView(View):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        return render(request,"Dish-list.html",{"items":qs})

class DishdetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dish=Dishes.objects.get(id=id)
        return render(request,"dish-detail.html",{"itm":dish})

class DishDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dish=Dishes.objects.get(id=id)
        dish.delete()
        return redirect("dish-list")
        



