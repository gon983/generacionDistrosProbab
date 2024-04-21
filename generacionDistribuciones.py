from funciones import *
import math

def generar_dist_uniforme():
    cant_n_deseados, lim_inf, lim_sup = pedir_parametros("Ingrese el limite inferior: ", "Ingrese el limite superior: ")
    v = []
    for i in range(0, cant_n_deseados):
        x = lim_inf + random.random() * (lim_sup-lim_inf)
        x_redondeado = round(x, ndigits=4)
        v.append(x_redondeado)

    return v


def generar_dist_exponencial():
    cant_n_deseados, media = pedir_parametros("Ingrese la media deseada: ")
    v = []

    for i in range(0, cant_n_deseados):
        x = -media * math.log((1 - random.random()), math.e)
        x_redondeado = round(x, ndigits=4)
        v.append(x_redondeado)

    return v

