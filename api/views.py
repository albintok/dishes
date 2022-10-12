from django.shortcuts import render
from django.views.generic import View
from api.models import Dishes

# Create your views here.

# localhost:8000/dishs/
class DishView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"dish.html")
    
    def post(self,request,*args,**kwargs):
        dname=request.POST.get("name")
        dprice=request.POST.get("price")
        dinage=request.POST.get("img")
        Dishes.objects.create()
        dname=request.POST.get("name")



