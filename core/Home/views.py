from django.shortcuts import render, redirect
from django.views.generic import View
from .toolConverter import toolVideo

# Create your views here.

URLYOUTUBE = []

class Home(View):
    
    def get(self, request):
        # Renderiza el template 'home.html' para solicitudes GET
        return render(request, 'home.html')

    def post(self, request):
        URLYOUTUBE.append(request.POST.get('urlYoutube', ''))
        
        action = request.POST.get('action', '')
        
        if action == 'form1':
            urlVideo = toolVideo(URLYOUTUBE[0])

            urlVideo.Info()
            context = {
                'calidadAudio': urlVideo.listaAudio,
                'calidadVideo': urlVideo.listaVideo,
                'titulo': urlVideo.title
            }
            return render(request, 'download.html', context)

        elif action == 'form2':

            urlVideo = toolVideo(URLYOUTUBE[0])
            urlVideo.Info()
            urlVideo.download(1,1,2)
        
        return redirect('home:home')
    
class Download(View):

    def get(self, request):

        return render(request, 'download.html')