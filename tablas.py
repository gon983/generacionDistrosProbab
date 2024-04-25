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
    v = [0] * len(intervalos)
    for i in range(0, len(serie)):
        n = serie[i]
        for j in range(0, len(intervalos)):
            if n < intervalos[j][1] and n >= intervalos[j][0]:
                v[j] += 1
    return v

# Llama a la funcion correspondiente segun la distribucion solicitada
# Y retorna el resultado que le envia esta funcion
def frecuencia_esperada(distrib, n_muestra, intervalos, parametros):

    if distrib == 1:
        return fe_uniforme(n_muestra,len(intervalos))
    elif distrib == 2:
        return fe_exponencial(n_muestra,intervalos, parametros)
    else:
        return fe_normal(n_muestra, intervalos, *parametros)
    
    
# Devuelve una lista con las frecuencias esperadas para una distr uniforme
def fe_uniforme(n, cant_intervalos):
    return [round(n/cant_intervalos, ndigits=4)] * cant_intervalos


# Devuelve una lista con las frecuencias esperadas para una distr normal
def fe_normal(n, intervalos, *parametros):
    
    media, desviacion = parametros
    frecuencias = []

    for intervalo in intervalos:
        marca_clase = round((intervalo[0]+intervalo[1])/2, ndigits=4)
        densidad = (math.e ** (-0.5 * ((marca_clase - media) / desviacion) ** 2)) / (desviacion * math.sqrt(2 * math.pi)) 
        densidad = densidad * (intervalo[1]-intervalo[0])
        
        f_esperada = densidad * n
        frecuencias.append(round(f_esperada, 4))
        
    return frecuencias


# Devuelve una lista con las frecuencias esperadas para una distr exponencial
def fe_exponencial(n, intervalos, parametros):
    media = parametros[0]
    frecuencias = []
    
    for intervalo in intervalos:
        marca_clase = round((intervalo[0]+intervalo[1])/2, ndigits=4)
        # densidad =  (1/media) * math.e ** (-(1/media) * marca_clase) *  (intervalo[1]-intervalo[0])
        acumulacion = (1 - math.e ** (- (1/media) * intervalo[1])) - (1 - math.e ** (- (1/media) * intervalo[0]))
        
        f_esperada = acumulacion * n
        frecuencias.append(round(f_esperada, 4))
        
    return frecuencias
    
