# VOLTAJES

print ("DIGITE 3 VOLTAJES DIFERENTES PARA QUE EL PROGRAMA EJECUTE DEBIDAMENTE.")
v1 = int(input("Digite voltaje numero 1 :"))
v2 = int(input("Digite voltaje numero 2 :"))
v3 = int(input("Digite voltaje numero 3 :"))
prom = (v1+v2+v3)/3

if v1 == v2:
    print ("Los numeros deben ser diferentes")
elif v1 == v3: 
    print ("Los numeros deben ser diferentes")
elif v2 == v3:
    print ("Los numeros deben ser diferentes")
else:
    print(prom)

if prom <= int(115):
    print("VOLTAJE CORRECTO")
elif prom > int(115) and prom < int(220):
    print("ALTO VOLTAJE")
else:
    print("¡¡PELIGRO!!")