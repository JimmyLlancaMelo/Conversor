import yt_dlp
import re, uuid

class toolVideo:
    
    def __init__(self, url):
        self.url = url
        self.title = ""
        self.listaVideo = []
        self.listaAudio = []

    def Info(self):
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(self.url, download=False) # SE OBTIENE LA INFORMACION EN UN DICCIONARIO

            self.title = info['title']

            for i in info['formats']: # SE OBTIENEN VARIOS FORMATOS - formad_id, url, ext, acodec, vcodec, filesize, abr, etc

                self.listaVideo.append(i.get("height","desconocido")) # OPTENER CALIDAD DE 1080p 720p 480p 360p 240p
                self.listaAudio.append(i.get("abr","desconocido")) # OBTENER CALIDAD DE 320kbs 192kbs 128kbs
                
            # QUITAR DUPLICADOS
            self.listaVideo = list(set(self.listaVideo))
            self.listaAudio = list(set(self.listaAudio))

            # DEJAR NUMEROS Y DECIMALES
            self.listaVideo = list(i for i in self.listaVideo if isinstance(i,int))
            self.listaAudio = list(i for i in self.listaAudio if isinstance(i,float))
            
            # ORDENAR
            self.listaVideo.sort(reverse=True) # DE MAYOR A MENOR
            self.listaAudio.sort(reverse=True)
            
            # FILTRAR
            self.listaVideo = [i for i in self.listaVideo if i > 100] # ELIMINAMOS ELEMENTOS MENORES A 100
            del self.listaAudio[3:len(self.listaAudio)] # ELIMINAMOS ELEMENTOS A PARTIR DEL INDICE 3 EN ADELANTE
            self.listaAudio[:3] = [320,192,128] # REEMPLAZAMOS LOS ELEMENTOS
            
            print(self.listaVideo)
            print(self.listaAudio)

    def download(self, choice1, choice2):
        unique_id = str(uuid.uuid4())  # Generar un UUID único
        
        if choice1 == 'mp3':
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': f'{self.listaAudio[int(choice2)]}',
                }],
                'extractaudio': True,
                'outtmpl': f'media/fileYoutube/%(title)s_{unique_id}.%(ext)s',
            }
            
        else:
            ydl_opts = {
                'format': f'bestvideo[height<={self.listaVideo[int(choice2)]}]+bestaudio/best',
                'merge_output_format': 'mp4',
                'outtmpl': f'media/fileYoutube/%(title)s_{unique_id}.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
                'postprocessor_args': [
                    '-c:v', 'copy',
                    '-c:a', 'aac',
                    '-b:a', '320k'
                ],
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
    
    def Iframe(self):
        
        match = re.search(r'(?:v=|\/|shorts\/|embed\/)([a-zA-Z0-9_-]{11})', self.url)
        if match:
            video_id = match.group(1)
            iframe_code = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
            return iframe_code
        return None

"""
url1 = 'https://www.youtube.com/shorts/c_ZBoufjaE0'
url2 = 'https://www.youtube.com/shorts/0Q8q89ZDuJ8'

video1 = toolVideo(url1)
video2 = toolVideo(url2)
video1.Info()
video2.Info()
video1.download('mp4',0)
video2.download('mp4',0)
"""