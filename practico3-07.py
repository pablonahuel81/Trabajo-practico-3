#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
vocales = ['a', 'e', 'i', 'o', 'u']
frase_palabra = input ("Escriba una frase o palabra usuario \n")
frase_palabra = frase_palabra.lower()
ultimo_caracter = frase_palabra [len(frase_palabra) -1]
if ultimo_caracter in vocales:
    print (frase_palabra + "!")
elif ultimo_caracter != vocales:
    print (frase_palabra)



