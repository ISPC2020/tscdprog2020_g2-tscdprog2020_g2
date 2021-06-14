# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:40:14 2021

@author: CarinaG
"""

#Proyecto general para trabajar con BD

'''def integradora:
    opcion==0
    print("Elija ña opción con la que desea trabajar: "):
    print(" 1 Clientes")
    print("2 Nueva Caja de Ahorro")
    print("3 Nuevo Palzo Fijo")
    print("4 Operar cuentas")
    print("5 Empleados")
    print("6 Cargar Sueldos")
    print("6 Salir")
    if opcion==1:
        Cliente()
    elif opcion==2:
        CajaAhorro()
    elif opcion==3:
        PlazoFijo()
    elif opcion==4:
        Operaciones()
    elif:
        Empleados()
    elif:
        CargarSueldos()
    else:
        print("Ingreso una opción no válida")
        
 
'''   
    
def Cliente(c):
    cliente=c
    validar="s"
    while validar=="s":
        print("Menú de opciones: ")
        print("Ingresa 1 para consultar la Base de datos de Cliente.")
        print("Ingresa 2 para dar de alta a un cliente.")
        print("Ingresa 3 para modificar los datos de un cliente.")
        print("Ingrese 4 para dar de baja a un cliente.")
        print("Ingrese opcion 5 para salir.")
        opcion=int(input("Ingrese su opción: "))
        if opcion==1:
            buscar_cliente()
        elif opcion==2:
            agregar_cliente()
        elif opcion==3:
            modificar_cliente()
        elif opcion==4:
            eliminar_cliente()
        elif opcion==5:
            print("Gracias")
        else:
            print("Ingresaste una opción no valida.")
        validar=input("Desea realizar otra operación en clientes: Ingrese s para SI / otra letra NO")
        if validar !="s":
            print("Gracias")
            
def Empleado(e):
    emp=e
    validar="s"
    while validar=="s":
        print("Menú de opciones: ")
        print("Ingresa 1 para consultar la Base de datos de Empleado.")
        print("Ingresa 2 para dar de alta a un empleado.")
        print("Ingresa 3 para modificar los datos de un empleado.")
        print("Ingrese 4 para dar de baja a un empleado.")
        print("Ingrese opcion 5 para salir.")
        opcion=int(input("Ingrese su opción: "))
        if opcion==1:
            buscar_emp()
        elif opcion==2:
            agregar_emp()
        elif opcion==3:
            modificar_emp()
        elif opcion==4:
            eliminar_empleado()
        elif opcion==5:
            print("Gracias")
        else:
            print("Ingresaste una opción no valida.")
        validar=input("Desea realizar otra operación en clientes: Ingrese s para SI / otra letra NO")
        if validar !="s":
            print("Gracias")

#def Cargar_sueldo()

                          
def buscar_cliente():  #método para buscar un cliente cuyo DNi lo ingreso por consola
        nro_DNI=int(input("Ingresa el DNI del cliente a consultar: "))
        if nro_DNI in cliente[0]:
            print("El cliente existe.")
            print("Nro de DNI: ",nro_DNI,"  Nombre:",cliente[nro_DNI][0],"  Mail:",cliente[nro_DNI][1],"  Tipo de Cuenta Bria:",cliente[nro_DNI][2],"  Monto:",cliente[nro_DNI][3])
            return nro_DNI
        else:
            print("No existe cliente")

         
def agregar_cliente():  #método para agregar un cliente nuevo al dict
        print(".·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨")
        print("Ingrese los datos para dar de alta a un nuevo cliente.")
        nro_DNI=int(input("Ingresa el número de DNI del nuevo cliente: "))
        if nro_DNI not in cliente[0]:
            nombre=input("Ingresa el nombre del cliente: ")
            mail=input("Ingresa el correo electrónico: ")
            tipo_cta=input("Ingresa CA para cuenta Caja de Ahorro o PF para cuenta Plazo Fijo: ")
            monto=float(input("Ingresa el monto inicial: "))
            cliente=[nro_DNI,nombre.capitalize(),mail,tipo_cta.upper(),monto]
        else:
            print("El cliente ya existe.")
            
def modificar_cliente(): # método para modificar el mail del cliente
        print("Modificar mail de un Cliente")
        nro_DNI=int(input("Ingresa el nro de DNI del cliente para actualizar sus datos: "))
        if nro_DNI in cliente:
            mail=input("Ingresa el nuevo E-mail: ")
            cliente[2]=mail
            print("Los datos del cliente se han actualizados.")
            print("Nro DNI: ",cliente[0],"  Nombre:",cliente[1],"   E-mail: ",cliente[2])
        else:
            print("No existe cliente.")
            
def eliminar_cliente():  #creo el método para eliminar un cliente ingresando su nro de DNI
         nro_DNI=int(input ("Ingresa el número de DNI del Cliente que deseas eliminar:  "))
         
         if nro_DNI in cliente[0]:  #verifico si el DNI existe y en caso positivo elimina el registro
            del cliente
            print("Se elimino con éxito el Cliente de la Base de Datos")
         else:
            print("El Cliente no existe en la Base de Datos.")



def agregar_emp():  #creo la clase Agregar empleado
        print("Ingrese los datos para dar de alta a un nuevo Empleado.")
        nro_emp=int(input("Ingresa el número de empleado: "))  #voy ingresando los datos de los empleados
        if nro_emp not in empleados[0]:
            nombre=input("Ingresa el nombre: ")
            apellido= input("Ingresa el apellido: ")
            genero=input("Ingresa M para Masculino o F para Femenino: ")
            telefono=int(input("Ingresa el número de teléfono: "))
            ingreso=input("Ingrese la fecha de ingreso a la empresa, formato dd/mm/aaaa: ")
            empleados=[nro_emp,nombre.capitalize(),apellido.capitalize(),genero.upper(),telefono,ingreso]  #cargo los datos en el diccionario
        else:
            print("El empleado ya existe en Base de datos.")
        
def mostrar_emp():  #creo el método mostrar sucursales recorriendo el diccionario por cada numero de sucursal
       for nro_emp in empleados[0]:  #recorro el diccionario mostrando los datos de la sucursal           
           print("Nro de Empleado: ",nro_emp[0],"  Nombre:",empleados[1],"  Apellido:",empleados[2],"  Genero:",empleados[3],"  Teléfono:",empleados[4])
           
           print("--------------------------------------")
           
def buscar_emp():
    nro_emp=int(input ("Ingresa el número de empleado que deseas consultar:  "))
    if nro_emp in empleados[0]:
        print("Nro de Empleado: ",empleados[0],"  Nombre:",empleados[1],"  Apellido:",empleados[2],"  Genero:",empleados[3],"  Teléfono:",empleados[4])
        return nro_emp
    else:
        print("El empleado ingresado no existe.")

def modificar_emp(): #hacer
    print("Modificar mail de un Cliente")
    nro=int(input("Ingresa el nro de empleado para actualizar sus datos: "))
    if nro_emp in empleados:
        nom=input("Ingrese el nombre del empleado: ")
        ape=input("Ingrese el apellido: ")
        gen=input("Ingrese el genero: ")
        print("Los datos del empleado se han actualizados.")
        print("Nro Emp: ",empleados[0],"  Nombre:",empleados[1],"   Apellido: ",cliente[2])
    else:
        print("No existe empleado con ese número.")

             
           
def eliminar_empleado():
    nro_emp=int(input ("Ingresa el número de empleado que deseas eliminar:  "))         
    if nro_emp in empleados:
        del empleados[nro_emp]
        print("Se elimino con éxito el empleado de la Base de Datos")
    else:
        print("El empleado no existe en la Base de Datos.")

    


empleados=[[1,"Agustín","Calvo","M",351269870,"25/08/1980"],[2,"Andrea","Juarez","F",357356980,"10/02/1996"],[3,"Anabela","Ruiz","F",34129870,"18/05/2005"]]     
cliente=[[236541,"Carlos Fuentes","carlitos@yahoo.com","CA",98000],[45639,"Carla Flores","carlita@gmail.com","PF",35000][3654125,"Rosa Roja","rosita@gmail.com","CA",365000]]
#i=integradora()
i=Cliente(cliente)
#e=Empleado(e)
#i.cargar_sueldo()
