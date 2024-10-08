from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render
from inicio.models import Auto

def mi_vista(request):
    return HttpResponse("Hola soy la vista")

def inicio(request):
    return render(request,'inicio/index.html')

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
    
    
    return render(request, "inicio/primer-template.html", datos)


def crear_auto(request, marca, modelo, anio):
    auto = Auto(marca=marca , modelo=modelo ,anio= anio) 
    auto.save()
    return render(request,"inicio/crear_auto.html", {'auto':auto})