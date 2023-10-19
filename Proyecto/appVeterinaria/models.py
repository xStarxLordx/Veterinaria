from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(primary_key= True,max_length=10)
    edad = models.CharField(max_length=2)
    rol = models.CharField(max_length=15, null=True)
    user = models.CharField(max_length=20, null=True)
    clave = models.CharField(max_length=50, null=True)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    cedula_dueño = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    edad = models.CharField(max_length=2)
    id = models.AutoField(primary_key = True)
    especie = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    caracteristicas = models.CharField(max_length=50)
    peso = models.CharField(max_length=3)
    

"""
class Historia_Clinica():
    def __init__(self):
        self.registros = {}      
    def agregar_registro(self, id_mascota, fecha, medico, motivo, 
                     sintomas, diagnostico, procedimiento, medicamento, 
                     dosis, id_orden, historial_vacunas, alergias, detalle):
        self.registros[id_mascota] = {}

        registro = {"Fecha": fecha, "Medico": medico, "Motivo": motivo,
                     "Sintomas": sintomas, "Diagnostico": diagnostico,
                      "Procedimiento": procedimiento, "Medicamento": medicamento,
                       "Dosis": dosis, "ID Orden": id_orden, "Historial de vacunas": historial_vacunas,
                        "Alergias": alergias, "Detalle": detalle}
        self.registros[id_mascota][fecha] = registro
"""
class Orden(models.Model):
    id_orden = models.AutoField(primary_key = True)
    id_mascota = models.ForeignKey(Mascota,on_delete=models.CASCADE)
    cedula_dueño = models.CharField(max_length=10)
    cedula_veterinario = models.CharField(max_length=10)
    nombre_medicamento = models.CharField(max_length=50,null=True)
    fecha = models.DateField(auto_now_add=True)
    anulada = models.BooleanField(null=True)

class Factura(models.Model):
    id_factura = models.AutoField(primary_key = True)
    id_mascota = models.ForeignKey(Mascota,on_delete=models.CASCADE)
    cedula_dueño = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_orden= models.ForeignKey(Orden,on_delete=models.CASCADE, null= True)
    nombre_producto = models.CharField(max_length=50,null=True)
    valor = models.FloatField(max_length=15)
    cantidad = models.IntegerField()

class Historia(models.Model):
    cedula_veterinario = models.CharField(max_length=10)
    id_mascota = models.ForeignKey(Mascota,on_delete=models.CASCADE)
    motivo = models.CharField(max_length=200)
    sintomas = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=500)
    procedimiento = models.CharField(max_length=500)
    id_orden = models.CharField(max_length=10,null=True)
    nombre_medicamento = models.CharField(max_length=50,null=True)
    vacunas = models.CharField(max_length=200)
    alergias = models.CharField(max_length=200)
    detalles = models.CharField(max_length=500)
    fecha = models.DateField(auto_now_add=True)

