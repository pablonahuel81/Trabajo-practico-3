#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre_usuario = input ("Ingrese su nombre usuario ")
print ("1. Si quiere su nombre en mayúsculas.")
print ("2. Si quiere su nombre en minúsculas.")
print ("3. Si quiere su nombre con la primera letra mayúscula.")
opcion_solicitada = int (input("Ingrese la opcion que mas le plazca "))
if opcion_solicitada == 1: 
    print ("su nombre usuario es :",nombre_usuario.upper ())
elif opcion_solicitada == 2:
    print ("su nombre usuario es ",nombre_usuario.lower())
elif opcion_solicitada == 3:
    print ("su nombre usuario es ", nombre_usuario.title())
else:
    print ("NO juegues conmigo jeje")

    



    
    