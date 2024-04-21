import random

def validar_entre_nums(li,ls, msj):
    a = int(input(msj))
    while a < li or a > ls:
        a = int(input(msj))
    return a



def pedir_parametros(msj1, msj2):
    cant_nums = validar_entre_nums(1, 1000000, "Ingrese la cantidad de numeros que quiera generar (menor al millon)")
    param2 = int(input(msj1))
    param3 = int(input(msj2))
    return cant_nums, param2, param3


def generar_dist_uniforme():
    cant_n_deseados, lim_inf, lim_sup = pedir_parametros("Ingrese el limite inferior", "Ingrese el limite superior")
    v = []
    for i in range(0, cant_n_deseados):
        x = lim_inf + random.random() * (lim_sup-lim_inf)
        v.append(x)

    return v



