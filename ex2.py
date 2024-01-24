# AREA TRIANGULO EQUILATERO = base * altura / 2

base = float(input("INGRESE BASE DEL TRIANGULO :"))
altura = float(input("INGRESE ALTURA DEL TRIANGULO :"))

area_T = (base * altura) / 2
if area_T > int(1000):
    print("DATOS NO VALIDOS")
else:
    print(area_T)
