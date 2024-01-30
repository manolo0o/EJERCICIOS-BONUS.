#nombre = str(input("Ingrese su nombre : "))
#print (f"Hola,{nombre}")


#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
import math
radio = int(input("INGRESE EL RADIO DEL CIRCULO :"))
Perimetro = 2 * math.pi * radio
print ("El perimetro del circulo es", Perimetro)
area = math.pi * radio**2
print ("El area del circulo es", area)
