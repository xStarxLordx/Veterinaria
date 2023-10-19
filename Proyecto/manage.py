#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
"""
from Veterinaria import clases
from controller import inputs
from controller import business
"""
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Veterinaria.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
"""
veterinaria = clases.Veterinaria()
veterinaria.admins.append(clases.admin0)
veterinaria.personas.append(clases.admin0)
veterinaria.veterinarios.append(clases.vet0)
veterinaria.personas.append(clases.vet0)
veterinaria.personas.append(clases.vendedor0)
veterinaria.vendedores.append(clases.vendedor0)
veterinaria.dueños.append(clases.dueño0)
veterinaria.personas.append(clases.dueño0)
business.agregar_mascota(veterinaria,"Pelusa","12345",7,"1","Gato","Persa","Negro",5)
business.agregar_historia(veterinaria,"29-03-2023","1","123456","Consulta","Ninguno","Sobrepeso","Bajar ingesta calórica"," "," ","1","123"," ","Sobrepeso")
business.agregar_historia(veterinaria,"29-04-2023","1","123456","Seguimiento","Ninguno","Sobrepeso","Bajar ingesta calórica"," ","","2 ","123"," ","Sobrepeso")
business.crear_orden(veterinaria,"1","1","12345","123456","Paracetamol","29-03-2023")
business.crear_orden(veterinaria,"2","1","12345","123456","Paracetamol","29-03-2023")
id_mascota = 2
id_orden = 3
id_factura = 2
"""
if __name__ == '__main__':
    main()
