from funciones import *
from generacionDistribuciones import *
from tablas import *

serie = generar_dist_uniforme()
print(serie)


intervalos = generar_intervalos(serie, 8)
print(intervalos)
frec = frecuencia_observada(serie , intervalos)
print(frec)

