from django.shortcuts import render, redirect
from django.views.generic import View
from .toolConverter import toolVideo

class Home(View):
    
    def get(self, request):
        return render(request, 'home.html')
    

    def post(self, request):
        
        action = request.POST.get('action', '')
        
        if action == 'form1':
            
            urlYoutube = request.POST.get('urlYoutube', '') 
            request.session['urlYoutube'] = urlYoutube
            
            urlVideo = toolVideo(urlYoutube)
            iframeC = urlVideo.Iframe()
            urlVideo.Info()
            context = {
                'calidadAudio': urlVideo.listaAudio,
                'calidadVideo': urlVideo.listaVideo,
                'titulo': urlVideo.title,
                'url': iframeC
            }
            return render(request, 'download.html', context)
        
        elif action == 'form2':
            
            urlYoutube = request.session.get('urlYoutube')
            indexG = request.POST.get('indexG','')
            formato = request.POST.get('format','')

            urlVideo = toolVideo(urlYoutube)
            urlVideo.Info()
            urlVideo.download(formato,indexG)
            
            return redirect('home:home')

class Download(View):
    def get(self, request):
        return render(request, 'download.html')