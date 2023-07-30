from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import tienda, producto
# Create your views here.

def productos(request):
    return render(request,'productos.html')

def tiendas(request):
    return render(request,'tiendas.html')

def registroTienda(request):
        if request.method=='POST':
             direccion = request.POST.get('direccion')
             provincia = request.POST.get('provincia')
             region = request.POST.get('region')
             fechaCreacion = request.POST.get('fechaCreacion')
             provincia = request.POST.get('provincia')
             telefono = request.POST.get('telefono')
             tienda.objects.create(
                  direccion=direccion,
                  provincia=provincia,
                  region=region,
                  fechaCreacion=fechaCreacion,
                  telefono=telefono)
             return HttpResponseRedirect(reverse('app2:ingresoTienda'))
        
        return render(request,'tiendas.html',{'listaTiendas':tienda.objects.all().order_by('id'),
                                              })
     