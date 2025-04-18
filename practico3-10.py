hemisferio = input("¿En qué hemisferio se encuentra Sir? (sur o norte): ").lower()
mes_año = input("Ahora, ¿en qué mes del año se encuentra Sir?: ").lower()
dia = int(input("Y, por último, ¿qué día es?: "))

if hemisferio == "sur":
    if (mes_año == "diciembre" and dia >= 21) or (mes_año == "enero") or (mes_año == "febrero") or (mes_año == "marzo" and dia <= 20):
        print("Se encuentra en Verano")
    elif (mes_año == "marzo" and dia >= 21) or (mes_año == "abrl") or (mes_año == "mayo") or (mes_año == "junio" and dia <= 20): 
        print ("Se encuentra en otoño")
    elif (mes_año == "junio" and dia >= 21) or (mes_año == "julio") or (mes_año == "agosto") or (mes_año == "septiembre" and dia <= 20):
        print ("Se encuentra en invierno")
    elif (mes_año == "septiembre" and dia >= 21) or (mes_año == "diciembre" and dia <= 20):
        print ("Se encuentra en primavera")
if hemisferio == "norte":
    if (mes_año == "diciembre" and dia >= 21) or (mes_año == "enero") or (mes_año == "febrero") or (mes_año == "marzo" and dia <= 20):
        print ("Se encuentra en invierno")   
    elif (mes_año == "marzo" and dia >= 21) or (mes_año == "abrl") or (mes_año == "mayo") or (mes_año == "junio" and dia <= 20): 
        print ("Se encuentra en primavera")
    elif (mes_año == "junio" and dia >= 21) or (mes_año == "julio") or (mes_año == "agosto") or (mes_año == "septiembre" and dia <= 20):
        print ("Se encuentra en verano")
    elif (mes_año == "septiembre" and dia >= 21) or (mes_año == "diciembre" and dia <= 20):
        print ("Se encuentra en otoño")
        
       
        


