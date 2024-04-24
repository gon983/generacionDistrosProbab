from funciones import *
from generacionDistribuciones import *
from tablas import *
import math
from prueba_bondad import *
import matplotlib.pyplot as plot


print("DISTRIBUCIONES")
print("1. Uniforme")
print("2. Normal")
print("3. Exponencial Negativa")
print("0. Salir")
distribucion = int(input("Ingrese la distribución que desea generar: "))
serie = []
parametros = []

while distribucion != 0:
    if distribucion == 1:
        serie = generar_dist_uniforme()

        cant_intervalos = int(input("Ingrese la cantidad de intervalos a utilizar (10, 12, 16, 23): "))

        print("\n\nIntervalos", "-" * 24)
        intervalos = generar_intervalos(serie, cant_intervalos)
        print(intervalos)

        print("\n\nFrecuencias observadas", "-" * 24)
        frecObservada = frecuencia_observada(serie, intervalos)
        print(frecObservada)

        print("\n\nFrecuencias esperadas", "-" * 24)
        frecEsperada = frecuencia_esperada(distribucion, len(serie), intervalos, parametros)
        print(frecEsperada)

        plot.hist(serie, bins=cant_intervalos, color="orange", edgecolor="white")
        plot.title("Distribucion uniforme")
        plot.ylabel("Frecuencia observada")
        plot.xlabel("Muestra")
        plot.show()

        print("-" * 24)
        print("1. Prueba de bondad de Chi Cuadrado")
        print("2. Prueba de bondad de KS")
        print("0. Salir")
        bondad = int(input("Seleccione la prueba de bondad a realizar: "))

        while bondad != 0:
            if bondad == 1:
                prueba = chi_cuadrado(intervalos, frecObservada, frecEsperada)
            elif bondad == 2:
                prueba = ks(intervalos, frecObservada, frecEsperada, len(serie))
            print("-" * 24)
            print("1. Prueba de bondad de Chi Cuadrado")
            print("2. Prueba de bondad de KS")
            print("0. Salir")
            bondad = int(input("Seleccione la prueba de bondad a realizar: "))



    elif distribucion == 2:
        cant_n, media, desviacion = pedir_parametros("Ingrese la media: ", "Ingrese la desviacion: ")
        serie= generar_dist_normal(cant_n, media, desviacion)
        parametros = [float(media), float(desviacion)]

        cant_intervalos = int(input("Ingrese la cantidad de intervalos a utilizar (10, 12, 16, 23): "))

        print("\n\nIntervalos", "-" * 24)
        intervalos = generar_intervalos(serie, cant_intervalos)
        print(intervalos)

        print("\n\nFrecuencias observadas", "-" * 24)
        frecObservada = frecuencia_observada(serie, intervalos)
        print(frecObservada)

        print("\n\nFrecuencias esperadas", "-" * 24)
        frecEsperada = frecuencia_esperada(distribucion, len(serie), intervalos, parametros)
        print(frecEsperada)

        plot.hist(serie, bins=cant_intervalos, color="orange", edgecolor="white")
        plot.title("Distribucion uniforme")
        plot.ylabel("Frecuencia observada")
        plot.xlabel("Muestra")
        plot.show()

        print("-" * 24)
        print("1. Prueba de bondad de Chi Cuadrado")
        print("2. Prueba de bondad de KS")
        print("0. Salir")
        bondad = int(input("Seleccione la prueba de bondad a realizar: "))

        while bondad != 0:
            if bondad == 1:
                prueba = chi_cuadrado(intervalos, frecObservada, frecEsperada)
            elif bondad == 2:
                prueba = ks(intervalos, frecObservada, frecEsperada, len(serie))
            print("-" * 24)
            print("1. Prueba de bondad de Chi Cuadrado")
            print("2. Prueba de bondad de KS")
            print("0. Salir")
            bondad = int(input("Seleccione la prueba de bondad a realizar: "))


    elif distribucion == 3:
        cant_n_deseados, media = pedir_parametros("Ingrese la media deseada: ")
        serie= generar_dist_exponencial(cant_n_deseados, media)
        parametros = [float(media)]

        cant_intervalos = int(input("Ingrese la cantidad de intervalos a utilizar (10, 12, 16, 23): "))

        print("\n\nIntervalos", "-" * 24)
        intervalos = generar_intervalos(serie, cant_intervalos)
        print(intervalos)

        print("\n\nFrecuencias observadas", "-" * 24)
        frecObservada = frecuencia_observada(serie, intervalos)
        print(frecObservada)

        print("\n\nFrecuencias esperadas", "-" * 24)
        frecEsperada = frecuencia_esperada(distribucion, len(serie), intervalos, parametros)
        print(frecEsperada)

        plot.hist(serie, bins=cant_intervalos, color="orange", edgecolor="white")
        plot.title("Distribucion uniforme")
        plot.ylabel("Frecuencia observada")
        plot.xlabel("Muestra")
        plot.show()

        print("-" * 24)
        print("1. Prueba de bondad de Chi Cuadrado")
        print("2. Prueba de bondad de KS")
        print("0. Salir")
        bondad = int(input("Seleccione la prueba de bondad a realizar: "))

        while bondad != 0:
            if bondad == 1:
                prueba = chi_cuadrado(intervalos, frecObservada, frecEsperada)
            elif bondad == 2:
                prueba = ks(intervalos, frecObservada, frecEsperada, len(serie))

            print("-" * 24)
            print("1. Prueba de bondad de Chi Cuadrado")
            print("2. Prueba de bondad de KS")
            print("0. Salir")
            bondad = int(input("Seleccione la prueba de bondad a realizar: "))

    print("-"*24)
    print("DISTRIBUCIONES")
    print("1. Uniforme")
    print("2. Normal")
    print("3. Exponencial Negativa")
    print("0. Salir")
    distribucion = int(input("Ingrese la distribución que desea generar: "))


