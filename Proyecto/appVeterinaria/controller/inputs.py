import business

def iniciar_sesion(veterinaria, rol):
    print("Inicia validacion")
    usuario = input("Ingrese el nombre de usuario: ")
    clave = input("Ingrese la clave: ")
    if usuario==None or usuario=="":
        print("el nombre de usuario no puede ser vacio")
        return False
    if clave==None or clave=="":
        print("la clave no puede ser vacio")
        return False
    print("pasa validacion")
    return business.iniciar_sesion(veterinaria, usuario, clave, rol)
    """if business.iniciar_sesion(veterinaria, usuario, clave, rol) == True:
        return True
    else:
        return False
    """
    
def agregar_persona(veterinaria, cedula, nombre, edad, rol, usuario, clave):
    if nombre==None or nombre=="" or nombre==" ":
        print("el nombre no puede ser vacio")
        return
    if cedula==None or cedula=="" or cedula==" ":
        print("la cedula no puede ser vacio")
        return
    if edad==None or edad=="":
        print("la edad no puede ser vacio")
        return
    if usuario==None or usuario=="" or usuario=="":
        print("el nombre de usuario no puede ser vacio")
        return 
    if clave==None or clave=="" or clave==" ":
        print("la clave no puede ser vacio")
        return 
    business.agregar_persona(veterinaria, cedula, nombre, edad, rol, usuario, clave)
    
def agregar_dueño(veterinaria, nombre, cedula, edad):
                            
    if nombre==None or nombre=="" or nombre==" ":
        print("el nombre no puede ser vacio")
        return
    if cedula==None or cedula=="" or cedula==" ":
        print("la cedula no puede ser vacio")
        return
    if edad==None or edad=="":
        print("la edad no puede ser vacio")
        return
    business.agregar_dueño(veterinaria, cedula, nombre, edad)
    
