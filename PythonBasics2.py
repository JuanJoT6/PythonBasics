#Librerias

import time

#Funciones (Ejercicios)

def Ej1():
    print("Altura")

    A = int(input("Ingrese la Altura de la persona en cm: "))
    
    if A < 170:
        print("Persona de estatura baja")
    else:
        print("Persona de estatura alta")
    
    time.sleep(3)

    #Volver al menu
    VM()


def Ej2():
    
    print("Salario")
    
    VD = int(input("Ingrese el valor del dia: "))
    CL = int(input("Ingrese la cantidad de dias laborados: "))
    S = VD * CL

    if S >= 100000:
        SD = round(S * 0.07, 2)
        ST = S - SD
        
        print("El salario equivale a: ", S)
        print("El descuento del salario equivale a: ", SD)
        print("El valor total a pagar es: ", ST)
    else:
        SD = S * 0
        ST = S - SD

        print("El salario equivale a: ", S)
        print("El descuento del salario equivale a: ", SD)
        print("El valor total a pagar es: ", ST) 



    time.sleep(3)

    #Volver al menu
    VM()


def Ej3():
    print("Supermercado")

    V = int(input("Ingrese el valor de la compra del cliente: "))

    if V >= 500000:
        D = V * 0.3
        VT = V - D
        print("El valor de la compra es de: ", V)
        print("El valor del descuento es de: ", D)
        print("El valor total a pagar es de: ", VT)
    else:
        D = V * 0.1
        VT = V - D
        print("El valor de la compra es de: ", V)
        print("El valor del descuento es de: ", D)
        print("El valor total a pagar es de: ", VT)

    
    time.sleep(3)

    #Volver al menu
    VM()


def Ej4():
    print("Camisas")

    CC = int(input("Ingrese la cantidad de camisas: "))
    CV = int(input("Ingrese el valor de las camisas: "))

    if CC >= 3:
        VC = CC * CV
        CD = VC * 0.2
        VT = VC - CD
        print("El valor de la compra es de: ", VC)
        print("El valor del descuento es de: ", CD)
        print("El valor total a pagar es de: ", VT)
    else:
        VC = CC * CV
        CD = VC * 0.1
        VT = VC - CD
        print("El valor de la compra es de: ", VC)
        print("El valor del descuento es de: ", CD)
        print("El valor total a pagar es de: ", VT)
    
    time.sleep(3)

    #Volver al menu
    VM()


def Ej5():
    print("Ventas")

    V = int(input("Ingrese el total de las ventas: "))

    if V >= 1000000:
        B = V * 0.20
        VT = V + B 
        print("La bonificacion tiene un valor de: ", B)
        print("El valor total a pagar es de: ", VT)
    else:
        B = V * 0.10
        VT = V + B
        print("La bonificacion tiene un valor de: ", B)
        print("El valor total a pagar es de: ", VT)

    #Volver al menu
    VM()

#Volver al menu
def VM():
    UserI = input("¿Quieres elegir otro ejercicio?\n")
    if UserI == "Si":
        Menu()
    elif UserI == "si":
        Menu()
    else:
        return()

#Menu

def Menu():
    SEJ = input("Seleccione un ejercicio: ")

    if SEJ == "1":
        Ej1()
    elif SEJ == "2":
        Ej2()
    elif SEJ == "3":
        Ej3()
    elif SEJ == "4":
        Ej4()
    elif SEJ == "5":
        Ej5()
    else:
        print("La entrada es invalida, intentalo de nuevo")
        Menu()

Menu()
