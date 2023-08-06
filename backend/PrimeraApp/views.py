from django.shortcuts import render, HttpResponse
from PrimeraApp.models import Articulo, Categoria
from PrimeraApp.FormArt import FormArt

# Create your views here.
def Home(req):
    return render(req, 'index.html')

def Contactame(req):
    return render(req, 'Contactame.html')

def RedesSociales(req):
    return render(req,'RedesSociales.html')

def CrearArticulo(req):
    Articlos = Articulo(
        titulo = "titulo",
        contenido = "libro escrito por ¡Dross",
        publico = True,
        
    )
    Articlos.save()
    return HttpResponse(f"Articulo creado: {Articlos.titulo}")

def FormArticulo(req):
    if req.method == 'POST':
        formulario = FormArt(req.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            titulo = data_form.get('titulo')
            contenido = data_form.get('contenido')
            publicado = data_form.get('publicado')
            Articlos = Articulo(
                titulo = titulo,
                contenido = contenido,
                publico = publicado,
        
                )
            
            Articlos.save()
            msj = f"{titulo} - {contenido} - {publicado}"
            print(msj)
    else:
        formulario = FormArt()        
    
    return render(req,'FormArt.html',{'form':formulario})

def ObtenerArticulo(req):
    try:
        #ObjArt = Articulo.objects.get(titulo = "Luna de Pluton", publico = True)
        ObjArt = Articulo.objects.get(pk=1)
        res = f"articulo: id:{ObjArt.id} - nombre:{ObjArt.titulo}"
    except Exception as e:
        res = f"articulo no encontrado. Error: {e}"
    return HttpResponse(res)

def actualizarArticulo(req,id):
    try:
        obj = Articulo.objects.get(pk=id)
        obj.titulo = "luna nomas"
        obj.contenido = "actualizado"
        obj.publico = True
        obj.save()
        msj = f"actualizado correcto el id: {obj.id}"
    except Exception as e:
        msj = f"Error al actualizar {e}"
    return HttpResponse(msj)