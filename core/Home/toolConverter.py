import yt_dlp

class toolVideo:
    
    def __init__(self, url):
        self.url = url
        self.listaVideo = []
        self.listaAudio = []

    def Info(self):
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(self.url, download=False) # SE OBTIENE LA INFORMACION EN UN DICCIONARIO

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

    def download(self, choice1, choice2,choice3):
        
        if choice1 == 1:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': f'{self.listaAudio[choice2]}',
                }],
                'extractaudio': True,
                'outtmpl': '%(title)s.%(ext)s',
            }
            
        else:
            ydl_opts = {
                'format': f'bestvideo[height<={self.listaVideo[choice3]}]+bestaudio/best',
                'merge_output_format': 'mp4',
                'outtmpl': '%(title)s.%(ext)s',
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

call = toolVideo('https://www.youtube.com/watch?v=Bma-C2lposk')
call.Info()
choice1 = int(input("Selecciona la calidad para descargar: "))
choice2 = int(input("Elige la calidad de audio: "))
choice3 = int(input("Elige la calidad de video: "))
call.download(choice1,choice2,choice3)
