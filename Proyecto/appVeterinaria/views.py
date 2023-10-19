from django.shortcuts import render,redirect
from django.http import HttpResponse
from .controller.business import agregar_persona
from .controller.business import *
from appVeterinaria.models import Usuario
from django.contrib import messages
from django.contrib.messages import constants as messages
# Create your views here.

def registroPersona(request,user):
    veterinario=Usuario.objects.get(user=user)
    return render(request,"Registrar.html",{"veterinario":veterinario})
def registroPersonaExitoso(request,user):
    veterinario=Usuario.objects.get(user=user)
    return render(request,"Registrar.html",{"mensaje":True}) 
def registroPersonaFallido(request):
    return render(request,"Registrar.html",{"mensaje":False}) 
def registroMascotaExitoso(request,user):
    veterinario = Usuario.objects.get(user = user)
    return render(request,"registrarMascota.html",{"mensaje":True,"veterinario":veterinario}) 
def registroMascotaFallido(request,user):
    veterinario = Usuario.objects.get(user = user)
    return render(request,"registrarMascota.html",{"mensaje":messages.ERROR,"veterinario":veterinario}) 
def registrar(request):
    try:
        cedula=request.GET["cedula"]
        nombre=request.GET["nombre"]
        edad = request.GET["edad"]
        agregar_persona(cedula,nombre,edad)
        return redirect("/registroPersonaExitoso/")
    except Exception as error:

        return redirect("/registroPersonaFallido/")
    
def registrarMascota(request):
    try:
        user = request.GET["user"]
        cedula=request.GET["cedula"]
        nombre=request.GET["nombre"]
        edad = request.GET["edad"]
        peso = request.GET["peso"]
        especie = request.GET["especie"]
        raza = request.GET["raza"]
        caracteristicas = request.GET["caracteristicas"]
        agregar_mascota(cedula, nombre, edad, peso, especie, raza, caracteristicas)
        return redirect("/registroMascotaExitoso/"+user)
    
    except Exception as error:
        
        return redirect("/registroMascotaFallido/"+user)
    
    
def iniciar(request):
    user = request.GET["user"]
    clave = request.GET["clave"]
    rol=request.GET["rol"]
    if(rol == "Veterinario"):
        try:
            Usuario.objects.get(user=user, clave=clave, rol=rol)
            return redirect("/inicioVet/"+user)
        except:
            return redirect("/iniciarSesionFallido/")
    if(rol == "Vendedor"):
        try:
            Usuario.objects.get(user=user, clave=clave, rol=rol)
            return redirect("/inicioVendedor/"+user)
        except Exception as error:
            return redirect("/iniciarSesionFallido/")
def nuevaOrden(request):
    try:
        cedula_veterinario = request.GET["cedula_veterinario"]
        id_mascota = request.GET["id_mascota"]
        cedula_dueño = request.GET["cedula_dueño"]
        nombre_medicamento = request.GET["medicina"]
        crear_orden(id_mascota,cedula_dueño,cedula_veterinario,nombre_medicamento)
        return redirect("/crearOrdenExitoso/"+cedula_veterinario)
    except Exception as error:
        return redirect("/crearOrdenFallido/")

def anulacionOrden(request):
    try:
        cedula_veterinario = request.GET["cedula_veterinario"]
        id_mascota = request.GET["id_mascota"]
        cedula_dueño = request.GET["cedula_dueño"]
        fecha = request.GET["fecha"]
        anular_orden(id_mascota,cedula_dueño,fecha)
        return redirect("/anularOrdenExitoso/"+cedula_veterinario)
    except Exception as error:
        return redirect("/anularOrdenFallido/"+cedula_veterinario)

def busquedaOrden(request):  
        cedula = request.GET["cedula"]
        id_mascota = request.GET["id_mascota"]
        cedula_dueño = request.GET["cedula_dueño"]
        fecha = request.GET["fecha"]
        try:
            orden = Orden.objects.get(id_mascota=id_mascota,cedula_dueño=cedula_dueño, fecha = fecha)
        except:
            orden=None
        if orden == None:
            return redirect("/buscarOrdenFallido/"+cedula)
        return redirect("/buscarOrdenExitoso/"+cedula+"/"+str(orden.id_orden))

def venta(request):
    try:
        id_orden = request.GET["id_orden"]
        cedula_dueño = request.GET["cedula_dueño"]
        id_mascota = request.GET["id_mascota"]
        nombre_producto = request.GET["nombre_producto"]
        valor = request.GET["valor"]
        cantidad = request.GET["cantidad"]
        cedula_vendedor = request.GET["cedula"]
        realizar_venta(id_mascota,cedula_dueño,id_orden,nombre_producto,valor,cantidad)
        return redirect("/crearFacturaExitoso/"+cedula_vendedor)
    except Exception as error:
        return redirect("/crearFacturaFallido/"+cedula_vendedor)

def nuevaHistoria(request):
    try:
        cedula_veterinario = request.GET["cedula_veterinario"]
        id_orden = request.GET["id_orden"]
        id_mascota = request.GET["id_mascota"]
        motivo = request.GET["motivo"]
        sintomas = request.GET["sintomas"]
        diagnostico = request.GET["diagnostico"]
        procedimiento = request.GET["procedimiento"]
        nombre_medicamento = request.GET["nombre_medicamento"]
        vacunas = request.GET["vacunas"]
        alergias = request.GET["alergias"]
        detalles = request.GET["detalles"]
        print(cedula_veterinario, id_orden, id_mascota, motivo, sintomas, diagnostico, procedimiento,
                    nombre_medicamento, vacunas, alergias, detalles)
        crear_historia(cedula_veterinario, id_orden, id_mascota, motivo, sintomas, diagnostico, procedimiento,
                    nombre_medicamento, vacunas, alergias, detalles)
        print(cedula_veterinario, id_orden, id_mascota, motivo, sintomas, diagnostico, procedimiento,
                    nombre_medicamento, vacunas, alergias, detalles)
        return redirect("/crearHistoriaExitoso/"+cedula_veterinario)
    except Exception as error:
        return redirect("/crearHistoriaFallido/"+cedula_veterinario)
    
    
def crearHistoria(request,user):
    veterinario = Usuario.objects.get(user=user)
    return render(request,"crearHistoria.html",{"veterinario":veterinario})

def iniciarSesion(request): 
    return render(request,"IniciarSesion.html")
def iniciarSesionFallido(request): 
    return render(request,"IniciarSesion.html",{"mensaje":False})

def registroMascota(request,user):
    veterinario=Usuario.objects.get(user=user)
    return render(request,"registrarMascota.html",{"veterinario":veterinario})

def iniciarSesionVet(request,user):
    veterinario=Usuario.objects.get(user=user)
    return render(request,"Vet.html",{"veterinario":veterinario})

def iniciarSesionVendedor(request,user):
    vendedor = Usuario.objects.get(user=user)
    return render(request,"Vendedor.html",{"vendedor":vendedor})

def buscarOrden(request,cedula):
    persona=Usuario.objects.get(cedula=cedula)
    return render(request,"buscarOrden.html",{"persona":persona}) 
def buscarOrdenExitoso(request,cedula, id):
    persona=Usuario.objects.get(cedula=cedula)
    orden = Orden.objects.get(id_orden = id)
    return render(request,"buscarOrden.html",{"mensaje":True,"persona":persona,"orden":orden}) 
def buscarOrdenFallido(request,cedula):
    persona=Usuario.objects.get(cedula=cedula)
    return render(request,"buscarOrden.html",{"mensaje":False,"persona":persona}) 

def crearOrden(request,cedula):
    veterinario=Usuario.objects.get(cedula=cedula)
    return render(request, "crearOrden.html",{"veterinario":veterinario})
def crearOrdenExitoso(request,cedula):
    veterinario=Usuario.objects.get(cedula=cedula)
    return render(request,"crearOrden.html",{"mensaje":True,"veterinario":veterinario}) 
def crearOrdenFallido(request,cedula):
    veterinario=Usuario.objects.get(cedula=cedula)
    return render(request,"crearOrden.html",{"mensaje":False,"veterinario":veterinario}) 

def anularOrden(request,cedula):
    veterinario=Usuario.objects.get(cedula=cedula)
    return render(request, "anularOrden.html",{"veterinario":veterinario})
def anularOrdenExitoso(request,cedula):
    veterinario = Usuario.objects.get(cedula=cedula)
    return render(request,"anularOrden.html",{"mensaje":True,"veterinario":veterinario}) 
def anularOrdenFallido(request,cedula):
    veterinario = Usuario.objects.get(cedula=cedula)
    return render(request,"anularOrden.html",{"mensaje":False,"veterinario":veterinario}) 

def crearFactura(request, cedula):
    vendedor = Usuario.objects.get(cedula=cedula)
    return render(request,"crearFactura.html",{"vendedor":vendedor})
def crearFacturaExitoso(request,cedula):
    vendedor = Usuario.objects.get(cedula=cedula)
    return render(request,"crearFactura.html",{"mensaje":True,"vendedor":vendedor}) 
def crearFacturaFallido(request,cedula):
    vendedor = Usuario.objects.get(cedula=cedula)
    return render(request,"crearFactura.html",{"mensaje":False,"vendedor":vendedor})
def crearHistoriaExitoso(request,cedula):
    veterinario = Usuario.objects.get(cedula=cedula)
    return render(request,"crearHistoria.html",{"mensaje":True,"veterinario":veterinario}) 
def crearHistoriaFallido(request,cedula):
    veterinario = Usuario.objects.get(cedula=cedula)
    return render(request,"crearHistoria.html",{"mensaje":False,"veterinario":veterinario}) 