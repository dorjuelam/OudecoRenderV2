"""oudecowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
]

"""oudecoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accesonoautorizado/', views.accesonoautorizado, name='accesonoautorizado'),
    path('', views.inicio, name='inicio'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('cliente/', views.cliente, name='cliente'),
    path('cliente/create/', views.create_cliente, name='create_cliente'),
    path('cliente/<int:NID>/', views.detalle_cliente, name='detalle_cliente'),
    path('cliente/<int:NID>/eliminar', views.eliminar_cliente, name='eliminar_cliente'),
    path('signin/', views.signin, name='signin'),
    path('inicio/', views.inicio, name='inicio'),
    path('home/', views.home, name='home'), 
    path('vistacliente/', views.vistacliente, name='vistacliente'),
    path('listaclientes/', views.listaclientes, name='listaclientes'),
    
    #INGENIEROS
    path('ingeniero/', views.ingeniero, name='ingeniero'),
    path('ingeniero/create/', views.create_ingeniero, name='create_ingeniero'),
    path('ingeniero/<int:COD_ingeniero>/', views.detalle_ingeniero, name='detalle_ingeniero'),
    path('ingeniero/<int:COD_ingeniero>/eliminar', views.eliminar_ingeniero, name='eliminar_ingeniero'),
    path('listaingenieros/', views.listaingenieros, name='listaingenieros'),
    
    # PROYECTOS
    path('proyecto/', views.proyecto, name='proyecto'),
    path('proyecto/create/', views.create_proyecto, name='create_proyecto'),
    path('proyecto/<int:Codigo>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyecto/<int:Codigo>/eliminar', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('listaproyectos/', views.listaproyectos, name='listaproyectos'),
    
    # ACTIVIDADES
    path('actividad/', views.actividad, name='actividad'),
    path('actividad/create/', views.create_actividad, name='create_actividad'),
    path('actividad/<int:COD_actividad>/', views.detalle_actividad, name='detalle_actividad'),
    path('actividad/<int:COD_actividad>/eliminar', views.eliminar_actividad, name='eliminar_actividad'),
    path('listaactividades/', views.listaactividades, name='listaactividades'),
    
    # MONEDA
    path('moneda/', views.moneda, name='moneda'),
    
    # OLVIDE MI CONTRASEÑA
    path('olvidemicontrasena/', views.olvidemicontrasena, name='olvidemicontrasena'),
    
    # INGENIEROS
    path('signiningeniero/', views.signiningeniero, name='signiningeniero' ),
    path('homeusuario/', views.homeusuario, name='homeusuario' ),
    path('signupingeniero/', views.signupingeniero, name='signupingeniero'),
    
    # BITACORAS
    path('bitacora/', views.bitacora, name='bitacora'),
    path('bitacora/create/', views.create_bitacora, name='create_bitacora'),
    path('listabitacoras/', views.listabitacoras, name='listabitacoras'),
    path('bitacora/<int:COD_bitacora>/', views.detalle_bitacora, name='detalle_bitacora'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    #GENERAR REPORTE
    path('generarreporte/', views.generarreporte, name='generarreporte' ),
    path('balancegeneral/', views.balancegeneral, name='balancegeneral' ),
    path('cifrasproyecto/', views.cifrasproyecto, name='cifrasproyecto' ),
    path('cifrasactividad/', views.cifrasactividad, name='cifrasactividad' ),
    path('novedadescolaborador/', views.novedadescolaborador, name='novedadescolaborador' ),
    path('buscarbitacoras/', views.buscarbitacoras, name='buscarbitacoras' ),
    path('productividad/', views.productividad, name='productividad' ),
    path('bitacorasingeniero/<int:COD_ingeniero>/', views.bitacorasingeniero, name='bitacorasingeniero'),
    path('detallebitacoraregistrada/<int:COD_bitacora>/', views.detallebitacoraregistrada, name='detallebitacoraregistrada'),
    path('base/', views.base, name='base' ),
    
    
    
    # path('enviar_recordatorio/', views.enviar_recordatorio, name='enviar_recordatorio'),
# path('email/recordatorio_bitacora.html/', views.email.recordatorio_bitacora, name='recordatorio_bitacora.html'),

]