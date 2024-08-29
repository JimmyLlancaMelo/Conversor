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
            listaSinDuplicadosVideo = list(set(self.listaVideo))
            listaSinDuplicadosAudio = list(set(self.listaAudio))
            
            # DEJAR NUMEROS Y DECIMALES
            self.soloNumeroVideo = [i for i in listaSinDuplicadosVideo if isinstance(i,int)]
            self.soloNumeroAudio = [i for i in listaSinDuplicadosAudio if isinstance(i,float)]
            
            print(self.soloNumeroVideo)
            print(self.soloNumeroAudio)

    def download(self, choice, choice2,choice3):
        
        if choice == 1:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': f'{self.soloNumeroAudio[choice2]}',
                }],
                'extractaudio': True,
                'outtmpl': '%(title)s.%(ext)s',
            }
            
        else:
            ydl_opts = {
                'format': f'bestvideo[height<={self.soloNumeroVideo[choice3]}]+bestaudio/best',
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


# Ejemplo de uso
call = toolVideo('https://www.youtube.com/watch?v=VBKqpdmg0B4')
call.Info()
choice = int(input("Selecciona la calidad para descargar: "))
choice2 = int(input("Elige la calidad de audio: "))
choice3 = int(input("Elige la calidad de video: "))
call.download(choice,choice2,choice3)
