
from appVeterinaria.models import *
#Metodo para agregar personas dependiendo del rol

def agregar_persona(cedula, nombre, edad):
    try:
        usuario = Usuario.objects.get(cedula=cedula)
    except:
        usuario=None
    if usuario!= None:
        raise Exception("Ya existe un usuario con la cédula: "+cedula)
   
    usuario=Usuario()
    usuario.cedula=cedula
    usuario.nombre=nombre
    usuario.edad = edad
    usuario.save()
    return 


#Método para agregar mascotas
def agregar_mascota(cedula_dueño, nombre, edad, peso, especie, raza, caracteristicas):
    try:
        usuario = Usuario.objects.get(cedula=cedula_dueño)
    except:
        usuario=None
    if usuario == None:
        raise Exception("No existe un usuario con la cédula: "+cedula_dueño)
    if usuario != None:
        mascota=Mascota()
        mascota.cedula_dueño = usuario
        mascota.nombre = nombre
        mascota.edad = edad
        mascota.especie = especie
        mascota.raza = raza
        mascota.peso = peso
        mascota.caracteristicas = caracteristicas
        mascota.save()
    return

def crear_orden(id_mascota,cedula_dueño,cedula_veterinario, nombre_medicamento):
    try:
        usuario = Usuario.objects.get(cedula=cedula_dueño)
        mascota = Mascota.objects.get(id=id_mascota,cedula_dueño=cedula_dueño)
    except:
        usuario=None
    if usuario == None or mascota == None:
        raise Exception("Error")
    orden=Orden()
    orden.cedula_dueño = cedula_dueño
    orden.id_mascota = mascota
    orden.cedula_veterinario = cedula_veterinario
    orden.nombre_medicamento = nombre_medicamento
    orden.save()
    return
def anular_orden(id_mascota, cedula_dueño, fecha):
    try:
        orden = Orden.objects.get(id_mascota=id_mascota,cedula_dueño=cedula_dueño, fecha = fecha)
    except:
        orden=None
    if orden == None:
        raise Exception("Error")
    orden.anulada = True
    orden.save()
    return

def realizar_venta(id_mascota, cedula_dueño, id_orden, nombre_producto, valor, cantidad):
    try:
        orden = Orden.objects.get(id_mascota=id_mascota,cedula_dueño=cedula_dueño,id_orden=id_orden)
        dueño = Usuario.objects.get(cedula=cedula_dueño)
        mascota = Mascota.objects.get(id=id_mascota)
    except:
        orden=None
    if orden == None:
        raise Exception("Error")
    factura = Factura()
    factura.id_mascota = mascota
    factura.cedula_dueño = dueño
    factura.id_orden = orden
    factura.nombre_producto = nombre_producto
    factura.cantidad = cantidad
    factura.valor = valor
    factura.save()
    return

def crear_historia(cedula_veterinario, id_orden, id_mascota, motivo, sintomas, diagnostico,
                   procedimiento, nombre_medicamento, vacunas, alergias, detalles):
    try:
        veterinario = Usuario.objects.get(cedula=cedula_veterinario)
        mascota = Mascota.objects.get(id=id_mascota)
        print("pasa veterinario y mascota")
    except:
        mascota = None
    try:
        orden = Orden.objects.get(id_mascota=id_mascota,cedula_veterinario=cedula_veterinario,id_orden=id_orden)
        print("pasa orden")
    except:
        orden = None
    if mascota == None:
        print("error mascota")
        raise Exception("Error")
    historia = Historia()
    historia.cedula_veterinario = veterinario.cedula
    historia.id_mascota = mascota
    historia.motivo = motivo
    historia.sintomas = sintomas
    historia.diagnostico = diagnostico
    historia.procedimiento = procedimiento
    historia.id_orden = orden.id_orden
    historia.nombre_medicamento = nombre_medicamento
    historia.vacunas = vacunas
    historia.alergias = alergias
    historia.detalles = detalles
    historia.save() 
    return
    
    