
#CHI CUADRADO

def chi_cuadrado(intervalos, fo, fe):
    i = 0
    v = []
    ace = 0
    aco = 0
    contador = 0
    z = 0
    lim_inferior = None
    lim_superior = None
    while i < len(intervalos):
        if fe[i] < 5:
            z = i
            lim_inferior = intervalos[z][0]
            while z < len(fe):
                ace = fe[z] + ace
                aco = fo[z] + aco
                if ace >= 5:
                    lim_superior = intervalos[z][1]
                    break
                z = z + 1
            i = z
            if ace >= 5:
               v.append([[lim_inferior, lim_superior], aco, ace, None, None])

            else:
               v[len(v) - 1][0] = [lim_inferior, intervalos[i - 1][1]]
               v[len(v) - 1][1] = v[len(v) - 1][1] + aco
               v[len(v) - 1][2] = v[len(v) - 1][2] + ace

               contador = contador + 1

        else:
            v.append([intervalos[i], fo[i], round(fe[i], 4), None, None])
            lim_inferior = intervalos[i][0]

        i = i + 1 + contador
        contador = 0
        aco = 0
        ace = 0

    j = 0
    print("Intervalos  ", "Frecuencia Ob.  ", "Frecuencia Esp.  ", "C          ", "C(AC)       ")
    while j < len(v):
        fe = v[j][2]
        fo = v[j][1]
        v[j][3] = round(((fe - fo)**2)/fe, 4)
        if j == 0:
            v[j][4] = v[j][3]
        else:
            v[j][4] = round(v[j][3] + v[j - 1][4], 4)
        print("-"*40)
        print(v[j])
        j = j + 1
    return v



#KS
def ks(intervalos, fo, fe, N):
    i = 0
    v = []
    while i < len(intervalos):
        v.append([intervalos[i], fo[i], round(fe[i], 4), round(fo[i]/N, 4), round(fe[i]/N, 4), None, None, None, None])
        i += 1
    j = 0
    print("Intervalos  ", "frecuencia ob. ", "frecuencia esp. ", "Probabilidad ob.  ", "Probabilidad esp. ", "Po(AC)    ", "Pe(AC)     ", "|Pe(AC) - Po(AC)|", "MAX(|Pe(AC) - Po(AC)|)")
    while j < len(v):
        if j == 0:
            v[j][5] = round(v[j][3], 4)
            v[j][6] = round(v[j][4], 4)
            v[j][7] = round(abs(v[j][5] - v[j][6]), 4)
            v[j][8] = round(v[j][7], 4)
        else:

            v[j][5] = round(v[j-1][5] + v[j][3], 4)
            v[j][6] = round(v[j-1][5] + v[j][4], 4)
            v[j][7] = round(abs(v[j][5] - v[j][6]), 4)
            if v[j][7] >= v[j - 1][8]:
                v[j][8] = round(v[j][7], 4)
            else:
                v[j][8] = round(v[j - 1][8], 4)

        print(v[j])
        print("-"*40)
        j += 1
    print("-"*50)
    print("Valor del estadístico de prueba: " + str(v[len(v) - 1][8]))
    return v



#[150.0321, 150.0371], [150.0371, 150.0421], [150.0421, 150.0471], [150.0471, 150.0521], [150.0521, 150.0571]]