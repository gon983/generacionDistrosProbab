from funciones import *
from generacionDistribuciones import *
from tablas import *
import math

print("DISTRIBUCIONES")
print("1. Uniforme")
print("2. Normal")
print("3. Exponencial Negativa")
distribucion = input("Ingrese la distribución que desea generar: ")
serie = []
parametros = []

if distribucion == "1":
    serie = generar_dist_uniforme()

elif distribucion =="2":
    cant_n, media, desviacion = pedir_parametros("Ingrese la media: ", "Ingrese la desviacion: ")
    serie= generar_dist_normal(cant_n, media, desviacion)
    parametros = [float(media), float(desviacion)]

elif distribucion == "3":
    cant_n_deseados, media = pedir_parametros("Ingrese la media deseada: ")
    serie= generar_dist_exponencial(cant_n_deseados, media)
    parametros = [float(media)]


cant_intervalos = int(input("Ingrese la cantidad de intervalos a utilizar (10, 12, 16, 23): "))


print("\n\nIntervalos","-"*24)
intervalos = generar_intervalos(serie, cant_intervalos)
print(intervalos)

print("\n\nFrecuencias observadas","-"*24)
frecObservada = frecuencia_observada(serie , intervalos)
print(frecObservada)

print("\n\nFrecuencias esperadas", "-"*24)
frecEsperada = frecuencia_esperada(distribucion, len(serie), intervalos, parametros)
print(frecEsperada)



