from funciones import *
from generacionDistribuciones import *
from tablas import *
import math
from prueba_bondad import *
import matplotlib.pyplot as plot

distribucion = serie = parametros = []

        
def generar_tabla(serie, distribucion, parametros):
    
    cant_intervalos = int(input("Ingrese la cantidad de intervalos a utilizar (10, 12, 16, 23): "))
    while cant_intervalos not in (10, 12, 16, 23):
        cant_intervalos = int(input("Elija una opción válida (10, 12, 16, 23): "))

    print("\n\nIntervalos", "-" * 24)
    intervalos = generar_intervalos(serie, cant_intervalos)
    print(intervalos)

    print("\n\nFrecuencias observadas", "-" * 24)
    frecObservada = frecuencia_observada(serie, intervalos)
    print(frecObservada)

    print("\n\nFrecuencias esperadas", "-" * 24)
    frecEsperada = frecuencia_esperada(distribucion, len(serie), intervalos, parametros)
    print(frecEsperada)

    return cant_intervalos, intervalos, frecObservada, frecEsperada


def generar_histograma(serie, distrib, frecuencia):
    
    #Esto es para que se siga ejecutando el codigo mientras esta la ventana del histograma abierta
    plot.ion()
    
    rango = [item for intervalo in intervalos for item in intervalo]
    rangoLabel = [str(el) for el in rango]
    
    plot.hist(serie, bins=rango, color="orange", edgecolor="white")

    for i, frecuencia in enumerate(plot.hist(serie, bins=rango, color="orange", edgecolor="white")[0]):
        
        # Esta division es para que me muestre las frecuencias por cada intervalo y no por cada limite del intervalo
        if i % 2 == 0:
            plot.text(rango[i], frecuencia, str(int(frecuencia)), ha='left', va='bottom')

    plot.xticks(rango, rangoLabel, rotation = 45)
    plot.title(distrib)
    plot.ylabel("Frecuencia observada")
    plot.xlabel("Intervalos")
    
    plot.show()
    
    
def pedir_prueba_a_realizar(intervalos, frecObservada, frecEsperada, serie, distribucion):
    bondad = ""
    while bondad != 0:
        print("1. Prueba de bondad de Chi Cuadrado")
        print("2. Prueba de bondad de KS")
        print("0. Volver al menú de distribuciones")
        bondad = int(input("Seleccione la prueba de bondad a realizar: "))
        if bondad == 1:
            aceptacion = chi_cuadrado(intervalos, frecObservada, frecEsperada, distribucion)
        elif bondad == 2:
            aceptacion = ks(intervalos, frecObservada, frecEsperada, len(serie))
        else:
            continue

        if aceptacion:
            print("El valor tabulado es mayor que el calculado. Por lo tanto, no se rechaza la hipótesis nula.")
        else:
            print("El valor calculado no es menor que el tabulado. Por lo tanto, se rechaza la hipótesis nula.")
        print("/" * 100)

        

while distribucion != 0:

    print("-"*24)
    print("DISTRIBUCIONES")
    print("1. Uniforme")
    print("2. Exponencial Negativa")
    print("3. Normal")
    print("0. Salir")
    distribucion = int(input("Ingrese la distribución que desea generar: "))

    if distribucion == 1:
        serie = generar_dist_uniforme()
        parametros = []
        titulo = "Distribucion Uniforme [a, b]"

    elif distribucion == 2:
        cant_n_deseados, media = pedir_parametros("Ingrese la media deseada: ")
        serie= generar_dist_exponencial(cant_n_deseados, media)
        parametros = [float(media)]
        titulo = "Distribucion Exponencial"

    elif distribucion == 3:
        cant_n, media, desviacion = pedir_parametros("Ingrese la media: ", "Ingrese la desviacion: ")
        serie= generar_dist_normal(cant_n, media, desviacion)
        parametros = [float(media), float(desviacion)]
        titulo = "Distribucion Normal"

    else:
        continue
    
    cant_intervalos, intervalos, frecObservada, frecEsperada = generar_tabla(serie, distribucion, parametros)
    if input("¿Mostrar serie? (s/n): ").lower() == "s": print(serie)
    if input("¿Mostrar histograma? (s/n): ").lower() == "s": generar_histograma(serie, titulo, frecObservada)
    
    print("-" * 24)
    print(f'La hipótesis nula es: "La muestra presenta una {titulo}"')
    pedir_prueba_a_realizar(intervalos, frecObservada, frecEsperada, serie, distribucion)
