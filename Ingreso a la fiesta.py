def ingresoFiesta():

    nombreAutorizado = ["Juan", "Roberto", "Camila", "Lautaro", "Adrián", "Micaela", "Florencia"]
    
    nombreDado = input ("Ingresar nombre")

    if nombreDado not in nombreAutorizado:

        print ("Negar Acceso")
        
    else: 
         print ("Paso siguiente")

def validarAcceso ():

    contraseña = "meEncantaPython"

    Contraseña = input ("Ingresar contraseña")

    if Contraseña != "meEncantaPython":
         print ("Negar acceso")
    else:
         print ("Paso siguiente")

def edad():
    edad = input ("Ingresar edad")
    edad = int (edad)

    if edad >= 18:
        print ("Permitir ingreso")
    else:
        print ("Negar acceso")
    
def numeroInvitado():

    numeroInvitado = [1, 3, 5, 6, 8, 99]   

    numeroDado = int (input("Ingresar número")) 

    if numeroDado not in numeroInvitado:
         print ("Rechazar acceso")
    else: 
         print ("Permitir acceso")
    

ingresoFiesta()
validarAcceso()
edad()
numeroInvitado()









