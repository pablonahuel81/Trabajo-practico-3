### 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string. 

contraseña = input("Ingrese contraseña, la misma debe tener entre 4 y 14 caracteres ")
longitud = len (contraseña)
if longitud >= 8 and longitud <= 14:
    print ("Usted ha ingresado una constraseña correcta")
else:
    print ("Por favor ingrese una contraseña correcta segun los parametros solicitados")
