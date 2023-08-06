from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import tienda, producto
# Create your views here.

def productos(request):
    return render(request,'productos.html')

def tiendas(request):
    return render(request,'tiendas.html')

def listarTiendaP(request,idTienda):             
     productoInformacion = producto.objects.get(tiendaProducto=idTienda)
     tiendaInformacion = tienda.objects.get(id=idTienda)
     return render(request,'verTiendas.html',{'productoInfo':productoInformacion,'tiendaInfo':tiendaInformacion})                                   
                                               
def registroTienda(request):
        if request.method=='POST':
             direccion = request.POST.get('direccion')
             provincia = request.POST.get('provincia')
             region = request.POST.get('region')
             fechaCreacion = request.POST.get('fechaCreacion')             
             telefono = request.POST.get('telefono')
             tienda.objects.create(
                  direccion=direccion,
                  provincia=provincia,
                  region=region,
                  fechaCreacion=fechaCreacion,
                  telefono=telefono)
             return HttpResponseRedirect(reverse('gestionTienda:registroTienda'))
        
        return render(request,'tiendas.html',{'listaTiendas':tienda.objects.all().order_by('id'),
                                              })
def eliminarTienda(request,idTienda):     
     tiendaEliminar= tienda.objects.get(id=idTienda)
     tiendaEliminar.delete()
     return HttpResponseRedirect(reverse('gestionTienda:registroTienda'))

def registroProducto(request):
        if request.method=='POST':
             descripcion = request.POST.get('descripcion')
             codigo = request.POST.get('codigo')
             precioVenta = request.POST.get('precioVenta')
             cantidad = request.POST.get('cantidad')                          
             producto.objects.create(
                  descripcion=descripcion,
                  codigo=codigo,
                  precioVenta=float(precioVenta),
                  cantidad=int(cantidad))
             return HttpResponseRedirect(reverse('gestionTienda:registroProducto'))
        
        return render(request,'productos.html',{'listaProductos':producto.objects.all().order_by('id'),
                                               'listaTiendas':tienda.objects.all().order_by('id'),
                                               })
def eliminarProducto(request,idProducto):     
     productoEliminar= producto.objects.get(id=idProducto)
     productoEliminar.delete()
     return HttpResponseRedirect(reverse('gestionTienda:registroProducto'))

def eliminarProductoVer(request,idProducto):     
     productoEliminar= producto.objects.get(id=idProducto)
     productoEliminar.delete()
     return HttpResponseRedirect(reverse('gestionTienda:registroTienda'))

def asignarTienda(request):
    if request.method == 'POST':
        idProducto = request.POST.get('productoSeleccionado')
        idTienda = request.POST.get('tiendaSeleccionado')
        objetoProducto = producto.objects.get(id=idProducto)
        objectoTienda = tienda.objects.get(id=idTienda)
        objetoProducto.tiendaProducto = objectoTienda
        objetoProducto.save()
    return HttpResponseRedirect(reverse('gestionTienda:registroProducto'))