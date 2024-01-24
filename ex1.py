# INGRESAR EN METROS Y VISUALIZAR EN KILOMETROS

#CONVERSOS METROS A KM
def convertidor_kilometros(distancia_Kms):

    distancia_Kms = distancia_Mtrs/ 1000
    return distancia_Kms

distancia_Mtrs = float(input("INGRESE LA DISTANCIA EN METROS :"))
distancia_Kms = convertidor_kilometros(distancia_Mtrs)

print(f"La distancia en kilometros es:{distancia_Kms}Kms")
