"""
URL configuration for Veterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from appVeterinaria.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('iniciarSesion/',iniciarSesion),
    path('registroPersona/<user>',registroPersona),
    path('registrar/', registrar ),
    path('registroPersonaExitoso/',registroPersonaExitoso),
    path('registroPersonaFallido/',registroPersonaFallido),
    path('inicioVet/<user>', iniciarSesionVet),
    path('inicioVendedor/<user>', iniciarSesionVendedor),
    path('iniciar/', iniciar),
    path('registroMascota/<user>', registroMascota),
    path('registrarMascota/', registrarMascota),
    path('registroMascotaExitoso/<user>', registroMascotaExitoso),
    path('registroMascotaFallido/', registroMascotaFallido),
    path('nuevaOrden/',nuevaOrden),
    path('crearOrden/<cedula>', crearOrden),
    path('crearOrdenExitoso/<cedula>/', crearOrdenExitoso),
    path('crearOrdenFallido/<cedula>/', crearOrdenFallido),
    path('iniciarSesionFallido/', iniciarSesionFallido),
    path('anulacionOrden/', anulacionOrden),
    path('anularOrden/<cedula>/', anularOrden),
    path('anularOrdenExitoso/<cedula>/', anularOrdenExitoso),
    path('anularOrdenFallido/<cedula>/', anularOrdenFallido),
    path('busquedaOrden/', busquedaOrden),
    path('buscarOrden/<cedula>/', buscarOrden),
    path('buscarOrdenExitoso/<cedula>/<id>/', buscarOrdenExitoso),
    path('buscarOrdenFallido/<cedula>/', buscarOrdenFallido),
    path('crearFactura/<cedula>/',crearFactura),
    path('venta/', venta),
    path('crearFacturaExitoso/<cedula>/', crearFacturaExitoso),
    path('crearFacturaFallido/<cedula>/', crearFacturaFallido),
    path('crearHistoria/<user>', crearHistoria),
    path('nuevaHistoria/', nuevaHistoria),
    path('crearHistoriaExitoso/<cedula>/', crearHistoriaExitoso),
    path('crearHistoriaFallido/<cedula>/', crearHistoriaFallido),
]
