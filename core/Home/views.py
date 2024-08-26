from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Home(View):

    def get(self,request,*args,**kwargs):
        context = {}
        return render(request,'home.html',context)
    
    def post(self,request,*args,**kwargs):
        pass
