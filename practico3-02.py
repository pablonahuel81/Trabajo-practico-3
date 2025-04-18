#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
aprobado = 6
nota_usuario = int(input("Ingrese su nota: "))
print ("La nota ingresada es: ", nota_usuario)
if nota_usuario >= aprobado:
    print ("Aprobado")
else:
    print ("Desaprobado Lince")
