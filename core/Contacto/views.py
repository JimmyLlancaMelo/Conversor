from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import EmailMessage  # Importar para enviar correo
from django.contrib import messages
from .forms import formContacto

class Contacto(View):

    def get(self, request, *args, **kwargs):
        form = formContacto()
        context = {
            'form': form
        }
        return render(request, 'contacto.html', context)

    def post(self, request, *args, **kwargs):
        form = formContacto(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # Enviar el correo electrónico
            subject = f'Nuevo mensaje de contacto: {nombre}'
            body = f'Nombre: {nombre}\nCorreo: {email}\n\nMensaje:\n{mensaje}'
            from_email = email  # El correo del remitente
            to_email = ['Windowsrevolutions501@gmail.com']  # El correo donde recibes los mensajes

            # Crear y enviar el correo
            email_message = EmailMessage(subject, body, from_email, to_email)
            email_message.send()

            # Mostrar un mensaje de éxito
            messages.success(request, 'Gracias por contactarnos. Te responderemos pronto.')

            return redirect('home:home')
        return render(request, 'contacto.html', {'form': form})
