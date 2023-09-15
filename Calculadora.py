
def calculadora():

    numeroIngresado = float (input("Ingresar primer valor"))

    numeroingresado2 = float (input("Ingresar segundo valor"))


    seleccion = float (input("suma(1), resta(2), multiplicacion(3), division(4)"))

    if seleccion == 1 :    
      resultado =  numeroIngresado + numeroingresado2
      print(resultado)
   
    if seleccion == 2: 
      resultado =   numeroIngresado - numeroingresado2
      print(resultado)
   
    if seleccion== 3:
      resultado = numeroIngresado * numeroingresado2
      print(resultado)

    if seleccion == 4:
      resultado = numeroIngresado / numeroingresado2
      print(resultado)




calculadora()

