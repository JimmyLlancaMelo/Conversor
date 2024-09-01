from django.urls import path
from .views import Home, Download

app_name = "home"

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('download/', Download.as_view(), name="download")
]