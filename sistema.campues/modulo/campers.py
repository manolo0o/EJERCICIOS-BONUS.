# CRUD

from .variables import save, getAll
import os
def create():
    os.system("clear")
    print(""" +++++++++++++++++++++++++
              + FORMULARIO DEL CAMPER +
              +++++++++++++++++++++++++
         """)
    save({
        "nombre":input("ingrese su nombre camper : "),
        "apellido":input("ingrese su apellido camper :"),
        "edad":input("Ingrese su edad camper :")
    })
    os.system("pause")
    
def read():
    
    
    
def update():
    print("El camper se actualizo")
    
def delete():
    print("El camper se borro")
    
def menu():
    menu = ["GUARDAR", "BUSCAR", "ACTUALIAZR", "ELMINAR", "SALIR"]
    while(True):
        os.system("clear")
        print(""" +++++++++++++++++++
              + MENU DEL CAMPER +
              +++++++++++++++++++
         """)
        print ("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc = int(input())
            if(opc <= len(menu) and opc>0):
                match(opc):
                    case 1: create()
                    case 2: read()
                    case 3: update()
                    case 4: delete() 
                    case 5: break    
        except ValueError:
            print(f"La opcion no esta habilitada")     