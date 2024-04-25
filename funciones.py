import random

def validar_entre_nums(li,ls, msj):
    a = int(input(msj))
    while a < li or a > ls:
        a = int(input(msj))
    return a



def pedir_parametros(msj1=None, msj2=None):
    cant_nums = validar_entre_nums(1, 1000000, "Ingrese la cantidad de numeros que quiera generar (menor al millon): ")
    if msj1 != None and msj2 == None:
        param2 = float(input(msj1))
        return cant_nums, param2
    if msj2 != None:
        param2 = float(input(msj1))
        param3 = float(input(msj2))
        return cant_nums, param2, param3
    return cant_nums


def calcular_promedio(v):
    suma = 0
    for i in range(0, len(v)):
        suma += v[i]

    return suma / len(v)
