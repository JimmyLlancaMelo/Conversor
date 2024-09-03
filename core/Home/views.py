from django.shortcuts import render, redirect
from django.views.generic import View
from .toolConverter import toolVideo
from django.http import FileResponse
from django.conf import settings
import os


class Home(View):
    
    
    def get(self, request,*args,**kwargs):
        
        return render(request, 'home.html')

    def post(self, request, *args, **kwargs):

        action = request.POST.get('action', '')
        
        if action == 'form1':
            urlYT2 = request.POST.get('urlYoutube', '')
            urlVideo = toolVideo(urlYT2)
            iframeC = urlVideo.Iframe()
            urlVideo.Info()
            print(urlYT2)
            context = {
                'calidadAudio': urlVideo.listaAudio,
                'calidadVideo': urlVideo.listaVideo,
                'titulo': urlVideo.title,
                'url': iframeC,
                'urlYT': urlYT2
            }
            return render(request, 'download.html', context)
        
        elif action == 'form2':
            YTurl = request.POST.get('urlMax', '')
            indexG = request.POST.get('indexG','')
            formato = request.POST.get('format','')
            
            print(f"ESTO ES LA URL QUE DEBERIA DE APARECER{YTurl}")

            urlVideo = toolVideo(YTurl)
            urlVideo.Info()
            urlVideo.download(formato,indexG)
            
            media = os.path.join(settings.MEDIA_ROOT, 'fileYoutube')
            title = urlVideo.title
            file_path = None

            
            for i in os.listdir(media):

                if i.startswith(title) and i.endswith(('.mp3', '.mp4')):
                    file_path = os.path.join(media, i) # ALMACENAMOS LA RUTA COMPLETA DEL ARCHIVO DESCARGADO
                    break

            if file_path and os.path.exists(file_path):
                filename = os.path.basename(file_path) # ALMACENAMOS EL NOMBRE COMPLETO CON LA EXTENCION
                response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
                return response
            
            else:
                return redirect('home:home')

class Download(View):
    def get(self, request):
        return render(request, 'download.html')