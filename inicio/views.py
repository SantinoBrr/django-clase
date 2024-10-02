from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render

def mi_vista(request):
    return HttpResponse("Hola soy la vista")

def inicio(request):
    return HttpResponse('<h1> Soy la pantalla de inicio </h1>')

def vista_datos1(request, nombre):
    nombre_mayuscula = nombre.upper()
    return HttpResponse(f'Hola {nombre_mayuscula}!!')

def primer_template(request):
    
    fecha_actual = datetime.now()
    datos = {
            "fecha_actual":fecha_actual,
            "numeros": list(range(1,11))
             }
    
    # VERSION 1 
    # template = loader.get_template("primer-template.html")
    # render_template = template.render(datos)
    
    
    return render(request, "primer-template.html", datos)