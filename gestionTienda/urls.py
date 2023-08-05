from . import views
from django.urls import path

app_name ='gestionTienda'

urlpatterns =[ 
 path('productos',views.registroProducto,name='registroProducto'), 
 path('',views.registroTienda,name='registroTienda'),
 path('eliminarTienda/<str:idTienda>',views.eliminarTienda,name='eliminarTienda'),
 path('eliminarProducto/<str:idProducto>',views.eliminarProducto,name='eliminarProducto'),
 path('asignarTienda',views.asignarTienda,name='asignarTienda'),
 path('listarTiendaP/<str:idTienda>',views.listarTiendaP,name='listarTiendaP'), 
]

 