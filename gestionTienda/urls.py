from . import views
from django.urls import path

app_name ='gestionTienda'

urlpatterns =[
 path('productos',views.productos,name='productos'),
 path('tiendas',views.tiendas,name='tiendas'),
 path('registroTienda',views.registroTienda,name='registroTienda')
]

 