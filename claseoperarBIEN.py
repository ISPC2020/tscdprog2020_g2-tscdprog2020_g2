# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:49:11 2021

@author: CarinaG
"""



def operar():
    cliente={236541:["Carlos Fuentes","carlitos@yahoo.com","CA",98000],456398:["Carla Flores","carlita@gmail.com","PF",35000],3654125:["Rosa Roja","rosita@gmail.com","CA",365000]}
 
    ganancia=0.8 
    dni=int(input("Ingrese el número del DNI para realizar la operación Bancaria: "))
    #for dni in cliente:
    if dni in cliente:    
        operacion=int(input("Ingrese la operación Bancaria: 1 -Depósito en CA / 2- Deposito en PF por 30 días/ 3  -Extracción : "))
            
        if operacion ==1:
            if cliente[dni][2]=="CA":
                mon=float(input("Ingrese el monto correspondientea depositar en su Caja de Ahorro: "))
                cliente[dni][3]=cliente[dni][3] + mon
                print("El saldo actual del cliente: ",dni,cliente[dni][0], " es: ",cliente[dni][3])
            else:
                print("El cliente no posee Caja de Ahorro y no puede operar sin una.")  #ver si agrego de abrir cuenta
        elif operacion==2:
            if cliente[dni][2]=="PF":
                mon=float(input("Ingrese el monto correspondientea depositar en Plazo Fijo por 30 días: "))
                cliente[dni][3]=cliente[dni][3] + mon +(mon * ganancia)
                print("El saldo actual del cliente: ",dni,cliente[dni][0], " es: ",cliente[dni][3])
            else:
                print("El cliente no tiene una cuenta Plazo Fijo y no puede eoprar sin una.")
        elif operacion==3:
            mon=float(input("Ingrese el monto que desea extraer de su cuenta: "))
            if cliente[dni][3] > mon:
                cliente[dni][3]=cliente[dni][3] - mon
                print("El saldo actual del cliente: ",dni,cliente[dni][0], " es: ",cliente[dni][3])
            else:
                print("El cliente no posee saldo suficiente para realizar la extracción.")
    else:
        print("No existe cliente.")
    
    opcion=int(input("Ingresa 1 para realizar otra operación Bancaria con cliente o 2 para terminar. Gracias. : "))
    if opcion==1:
       operar()    #Función recursiva
    else:
        print("Gracias por operar con nuestro banco.")               


o=operar()   
                    