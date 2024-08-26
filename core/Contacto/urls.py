from django.urls import path
from .views import Contacto

app_name = "contacto"

urlpatterns = [
    path('contacto/',Contacto.as_view(), name='contacto')
]