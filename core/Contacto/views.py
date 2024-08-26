from django.shortcuts import render
from django.views.generic import View

class Contacto(View):

    def get(self, request, *args,**kwargs):

        return render(request, 'contacto.html')
