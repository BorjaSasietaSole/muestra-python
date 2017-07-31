"""
Esto es un ejemplo de mi forma de trabajo:

Se muestra como crear una calcuadora en linea de comandos.

"""


""" funciones de calculo """


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b 


def dividir(a, b):
    return a / b


def resto (a, b):
    return a % b


"""funcion para pedir un valor y te devuelva forzando al usuario a que sea un entero"""
def pedir(cad):
    par = input(cad + "\n")
    par = int(par)
    while (type(par) != int):
        par = input("Error: el valor tiene de ser un número, " + cad + "\n")
    return par


salir = False
while(salir == False):
    palabra = input("que quieres hacer? (indica la palabra de la operación) \n")
    if (palabra == "sumar"):
        par1 = pedir("escribe el primer numero:")
        par2 = pedir("escribe el segundo numero:")
        print("El resultado de la operación es: " + str(sumar(par1, par2)) + "\n")
    elif (palabra == "restar"):
        par1 = pedir("escribe el primer numero:")
        par2 = pedir("escribe el segundo numero:")
        print("El resultado de la operación es: " + str(restar(par1, par2)) + "\n")
    elif (palabra == "multiplicar"):
        par1 = pedir("escribe el primer numero:")
        par2 = pedir("escribe el segundo numero:")
        print("El resultado de la operación es: " + str(multiplicar(par1, par2)) + "\n")
    elif (palabra == "dividir"):
        par1 = pedir("escribe el primer numero:")
        par2 = pedir("escribe el segundo numero:")
        print("El resultado de la operación es: " + str(dividir(par1, par2)) + "\n")
    elif(palabra == "resto"):
        par1 = pedir("escribe el primer numero:")
        par2 = pedir("escribe el segundo numero:")
        print("El resultado de la operación es: " + str(resto(par1, par2)) + "\n")
    elif(palabra == "salir"):
        salir = True
    else:
        print("No existe esta operación...\n")
print("Adios, fin del programa\n")
