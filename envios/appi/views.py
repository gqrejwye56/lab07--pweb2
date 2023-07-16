from django.shortcuts import render, HttpResponse

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



# Create your views here.

def enviar_correo(request):
    # Obtén los datos necesarios para el correo electrónico
    destinatario = 'gmartellv@unsa.edu.pe'
    asunto = 'Saludo'
    mensaje = 'Holaaaaaa'

    # Renderiza la plantilla del correo electrónico si es necesario
    # y obtén el contenido HTML y el contenido de texto sin formato
    html_message = render_to_string('email/correo.html', {'mensaje': mensaje})
    plain_message = strip_tags(html_message)
    # Envía el correo electrónico utilizando la función send_mail
    send_mail(asunto, plain_message, 'gmartellv@unsa.edu.pe', [destinatario], html_message=html_message)

    # Redirige a una página de éxito o muestra un mensaje de confirmación
    return HttpResponse('Correo electrónico enviado con éxito')
  
def home_view(request):
    # Contenido de la respuesta
    content = "¡Bienvenido a la página de inicio!"

    # Devolver una respuesta HTTP con el contenido
    return HttpResponse(content)