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


def generar_dist_exponencial(cant_n_deseados, media):
    v = []

    for i in range(0, cant_n_deseados):
        x = -media * math.log((1 - random.random()), math.e)
        x_redondeado = round(x, ndigits=4)
        v.append(x_redondeado)

    return v


def generar_dist_normal(cant_n, media, desviacion):
    if cant_n % 2 == 1:
        n_iteraciones = (cant_n // 2) + 1

    else:
        n_iteraciones = cant_n // 2
    v = []


    for i in range(0, n_iteraciones):
        rnd1 = random.random()
        rnd2 = random.random()
        x1 = (math.sqrt(-2 * math.log(rnd1, math.e)) * math.cos(2 * math.pi * rnd2)) * desviacion + media
        v.append(round(x1, ndigits=4))

        if (cant_n % 2 == 1) and i == (n_iteraciones - 1):
            break

        x2 = (math.sqrt(-2 * math.log(rnd1, math.e)) * math.sin(2 * math.pi * rnd2))* desviacion + media
        v.append(round(x2, ndigits=4))

    return v
