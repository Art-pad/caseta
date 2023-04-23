from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def mi_vista(request):
    return HttpResponse("Hola mundo")

def Pagina(request):
    plantillanueva = open("/Users/gerardo.padilla/accesoscaseta/Plantillas/Pagina.html")
    template = Template(plantillanueva.read())
    plantillanueva.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

 # def my_view(request):
   # if request.method == 'POST' and 'button_name' in request.POST:
    #    button_value = request.POST['button_name']
        # Realiza alguna acción basada en el valor del botón
    # return render(request, 'my_template.html')