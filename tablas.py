from funciones import *
import math

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
    for i in range(0, len(serie)):
        n = serie[i]
        for j in range(0, len(intervalos)):
            if n < intervalos[j][1] and n >= intervalos[j][0]:
                v[j] += 1
    return v


def frecuencia_esperada(distrib, serie, f_observada, intervalos, parametros):

    if distrib == "1":
        return fe_uniforme(len(serie),len(intervalos))
    elif distrib == "2":
        return fe_normal(len(serie), intervalos, *parametros )
    else:
        return fe_exponencial()
    

def fe_uniforme(n, cant_intervalos):
    return [round(n/cant_intervalos, ndigits=4)] * cant_intervalos


def fe_normal(n, intervalos, *parametros):
    
    media, desviacion = parametros
    frecuencias = []

    for intervalo in intervalos:

        marca_clase = round((intervalo[0]+intervalo[1])/2, ndigits=4)
        densidad =  (math.e ** (-0.5 * ((marca_clase - media) / desviacion) ** 2)) / ((desviacion * math.sqrt(2 * math.pi)) * (intervalo[1]-intervalo[0]))
        f_esperada = densidad * n
        frecuencias.append(f_esperada)
        
    return frecuencias

def fe_exponencial():
    pass

