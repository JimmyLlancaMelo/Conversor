from django.shortcuts import render, redirect
from django.views.generic import View
from .toolConverter import obtener_enlaces_descarga

# Create your views here.

class Home(View):
    
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        video_url = request.POST.get('video_url')
        
        if video_url:
            resultados = obtener_enlaces_descarga(video_url)
            return render(request, 'download.html', {
                'enlaces_mp4': resultados['mp4'],
                'enlaces_mp3': resultados['mp3'],
            })
        else:
            return render(request, 'home.html', {'error': 'Por favor, ingrese una URL válida.'})

class Download(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'download.html')
