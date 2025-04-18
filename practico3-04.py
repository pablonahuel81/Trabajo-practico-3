#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

print ("Ingrese su edad")
edad = int(input())
if edad < 12:
    print ("Pertenece a la categoria Niño/a")
elif edad > 12 and edad < 18: 
    print ("Pertenece a la categoria Adolescente")
elif edad > 18 and edad < 30:
    print ("Pertenece a la categoria adulto")
elif edad >= 30:
    print ("pertenece a la categoria adulto mayor o igual a 30")
    
