#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir en pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero_par = int(input("Ingresar un numero par, te estaremos vigilando: "))
if numero_par % 2 == 0:
    print ("El numero ingresado es par!")
else:
    print ("El numero ingresado no es par, te lo advertimos!")

    

