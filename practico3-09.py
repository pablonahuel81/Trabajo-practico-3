#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto = int(input("¿cual es la magnitud del terremoto? "))
magnitud_elegida = int(magnitud_terremoto)
if magnitud_elegida < 3:
    print ("Muy leve (imperceptible).")
elif (magnitud_elegida >=3) and (magnitud_elegida < 4):
    print ("Leve (ligeramente perceptible).") 
elif (magnitud_elegida >= 4) and (magnitud_elegida < 5):
    print ("Moderado (sentido por personas, pero generalmente no causa daños).")              
elif (magnitud_elegida >=5) and (magnitud_elegida < 6):
    ("Fuerte (puede causar daños en estructuras débiles).")
elif (magnitud_elegida >=6) and (magnitud_elegida < 7):
    print ("Muy Fuerte (puede causar daños significativos).")
elif magnitud_elegida >= 7:
    print ("Extremo (puede causar graves daños a gran escala).")
    
    
    
    

