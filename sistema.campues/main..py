import json
import os
#ayudas examen


with open('campers.json', 'r') as file1:
    camper = json.load(file1)

def guardarCampers(camper):
    with open('campers.json', 'w') as file:
        json.dump(camper, file, indent=4)
# AGREGAR CAMPER
def agregar():
    with open('campers.json', 'r') as file1:
        camper = json.load(file1)

    id = int(input("Ingrese el id del camper: "))
    
    for value in camper:
        if value["id"] == id:
            print("La ID ya está registrada. No se puede agregar el camper.")
            os.system('pause')
            return 
    inf = {
        "id": id,
        "name": input("Ingrese el nombre del camper: "),
        "apellido": input("Ingrese el apellido del camper: "),
        "adress": input("Ingrese direccion del camper: "),
        "acudent": input("Ingrese acudiente del camper (SOLO SI ES MENOR DE EDAD): "),
        "nro_cel": int(input("Ingrese número celular del camper:")),
        "nro_fij": int(input("Ingrese número fijo del camper (OPCIONAL):")),
        "fecha_ini": input("Ingrese fecha de incio: DD/MM/AA "),
    }
    print('Camper registrado')
    os.system('pause')
    camper.append(inf)
    guardarCampers(camper)


def guardarCampers(campers):
    with open('campers.json', 'w') as file2:
        json.dump(campers, file2, indent=2)

# Importar json y os en la parte superior de tu archivo
import json
import os

# Luego, puedes llamar a la función agregar() en tu programa principal


    
# ELIMINAR CAMPER

def deleteCamper():
    with open('campers.json','r') as file:
        camper = json.load(file)
    id = int(input("Ingrese id del camper a eliminar."))
    for i,value in enumerate(camper):
        if value["id"] == id:
            print(f'Id: {value["id"]} \nNombre: {value["name"]} \nApellido: {value["apellido"]}')      
            camper.pop(i)
            print("El camper ha sido eliminado satisfactoriamente.")
            guardarCampers(camper)
            os.system('pause')
            return
    print('Camper no existente.') 
    os.system('pause')  
    
# UPDATE INF CAMPER
def actualizarcamper(camper, id_camper):
    for i, value in enumerate(camper):
        if value.get('id') == id_camper:
                print(f'Datos actuales: \nNombre: {value["name"]} \nApellido {value["apellido"]} \nDirrección: {value["adress"]} \nAcudiente {value["acudent"]}\nNúmero celular: {value["nro_cel"]} \nNúmero Fijo: {value["nro_fij"]}')
                os.system('pause')
                msj = ("--- UPDATE ---")
                print(msj)
                n_name  = input("Ingrese el nombre del camper: "),    
                n_apellido = input("Ingrese el apellido del camper: "),    
                n_adress= input("Ingrese nueva direccion del camper: "),
                n_acudent = input("Ingrese nuev@ acudiente del camper (SOLO SI ES MENOR DE EDAD): "),
                n_nro_cel = int(input("Ingrese nuevo número celular del camper: ")),
                n_nro_fij = int(input("Ingrese nuevo número fijo del camper (OPCIONAL) : ")) ,
                n_fecha_ini = input("Ingrese nueva fecha de incio: "),
                n_jornada = input("Ingrese nueva jornada en la que estudiara el camper: ")
                
                value["name"] = n_name
                value["apellido"] = n_apellido
                value["adress"] = n_adress
                value["acudent"] = n_acudent
                value["nro_cel"] = n_nro_cel
                value["nro_fij"] = n_nro_fij
                value["fecha_ini"] = n_fecha_ini
                value["jornada"] = n_jornada
                print(f'Datos actualizados: \nNombre: {value["name"]} \nApellido {value["apellido"]} \nDirrección: {value["adress"]} \nAcudiente {value["acudent"]}\nNúmero celular: {value["nro_cel"]} \nNúmero Fijo: {value["nro_fijo"]}')
                
                guardarCampers(camper)
                return
    
    print('Camper no existente.')

def updateCamper():
    with open('campers.json', 'r') as file:
        camper = json.load(file)
    
    id_camper = int(input("Digite id del camper: "))
    
    actualizarcamper(camper, id_camper)
    os.system('pause')
    
# VER CAMPERS

def watchCampers():
    with open('campers.json','r') as file:
        camper = json.load(file)
    for i,value in enumerate(camper):
        print(f'Id: {value["id"]} \nNombre: {value["name"]} \nApellido: {value["apellido"]}')
    os.system('pause')
    
# VER CAMPER

def watchCamper():
    with open('campers.json','r') as file:
        camper = json.load(file)
    id= int(input("Ingrese id del camper a buscar: "))
    for i, value in enumerate(camper):
        if value["id"]== id:
            print(f'Id: {value["id"]} \nNombre: {value["name"]} \nApellido: {value["apellido"]}')
            os.system('pause')
            return
    print("No se encontró el camper.")
    os.system('pause')

    # SAVE CAMPER
    
def guardarCampers(camper):
    with open('campers.json', 'w') as file:
        json.dump(camper, file, indent=4)
