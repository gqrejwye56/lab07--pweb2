
from django.contrib import admin
from django.urls import path
from appi.views import enviar_correo, home_view

"""

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('enviar-correo/', enviar_correo, name='enviar_correo'),
    path('', home_view, name='home'),
]
