from datetime import date





# Definición de logones, roles y contraseñas
logon_roles_passwords = {
    "B959263": {"role": "SUPERIOR", "password": "CHIPI1971"},
    "C569853": {"role": "ADJUNTO", "password": "EURASIA"},
    "T698952": {"role": "TEMPORARIO", "password": "JAJAJANT"},
    "Z698563": {"role": "TERCERIZADO", "password": "ECHENME"}
}

# Definición de tipos de actos disponibles para cada rol
actos_disponibles = {
    "SUPERIOR": [1, 3, 4],
    "ADJUNTO": [1],
    "TEMPORARIO": [3, 1],
    "TERCERIZADO": [1, 5]
}

def login():
    max_attempts = 3

    while max_attempts > 0:
        logon = input("Ingrese su logon: ")
        if logon in logon_roles_passwords:
            role = logon_roles_passwords[logon]["role"]
            password = logon_roles_passwords[logon]["password"]
           

            while max_attempts > 0:
                entered_password = input("Ingrese su contraseña: ")
                if entered_password == password:
                    print("Login exitoso. Bienvenido, {}.".format(role))
                
                    print("Tipos de actos disponibles:", actos_disponibles[role])

                    continue
                
                elif role == "SUPERIOR":

                    actos_superior = actos_disponibles["SUPERIOR"]


                    acto = input ("Seleccione su acto: (actos_superior)")


                    if acto == "1"

                    print ("Completar formulario:")

                    date_fechaCierre = input (date("Ingrese la fecha de presentación"))

                    nombreEmpresa = input ("Ingrese el nombre de la empresa")
                    
                    date_fechaPresentacionDJ = input (date("Ingrese la fecha de presentación del DJ"))

                    #chequear si los tres datos fueron ingresados y mostrar un mensaje "Datos ingresados"
                    

                    return
                else:
                    print("Contraseña incorrecta. Intentos restantes:", max_attempts - 1)
                    max_attempts -= 1
            print("Ha excedido el número máximo de intentos.")
            return
        else:
            print("Logon incorrecto. Intentos restantes:", max_attempts - 1)
            max_attempts -= 1

    print("Ha excedido el número máximo de intentos.")


# Ejemplo de uso
login()
