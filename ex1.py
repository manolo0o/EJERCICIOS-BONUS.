# INGRESO DE VOLTAJES 
v1 = int(input("ingrese voltaje 1 : "))
v2 = int(input("ingrese voltaje 2 : "))
v3 = int(input("ingrese voltaje 3 : "))
v4 = int(input("ingrese voltaje 4 : "))
v5 = int(input("ingrese voltaje 5 : "))

prom = (v1 + v2 + v3 + v4 + v5) / 5 # CALCULO DE PROMEDIO
print (prom) # PROMEDIO

if prom > int(220) :
    print("ALTO VOLTAJE")
elif prom < int(220) :
    print ("VOLTAJE CORRECTO")
