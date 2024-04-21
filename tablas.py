from funciones import *

def generar_intervalos(serie, cantidad_intervalos):
    max = -99999999999999999999999999999999
    min = 99999999999999999999999999999999
    for i in range(0, len(serie)):
        if serie[i] > max:
            max = serie[i]
        if serie[i] < min:
            min = serie[i]

    rango = max - min
    amplitud = round(rango / cantidad_intervalos, ndigits=4)

    lim_inf = min
    lim_sup = round(min + amplitud, ndigits=4)
    intervalos = [[lim_inf, lim_sup]]

    for i in range(0, (cantidad_intervalos - 1)):
        lim_inf += amplitud
        lim_sup += amplitud
        intervalos.append([round(lim_inf, ndigits=4), round(lim_sup, ndigits=4)])

    return intervalos




def frecuencia_observada(serie, intervalos):
    v = vector_nulo(len(intervalos))
    print(v)
    for i in range(0, len(serie)):
        n = serie[i]
        for j in range(0, len(intervalos)):
            if n < intervalos[j][1] and n >= intervalos[j][0]:
                v[j] += 1


    return v
