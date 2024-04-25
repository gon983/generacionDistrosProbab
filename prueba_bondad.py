from valores import *

#CHI CUADRADO
def chi_cuadrado(intervalos, fo, fe, distr):
    i = 0
    v = []
    ace = 0
    aco = 0

    z = 0
    lim_inferior = intervalos[0][0]
    lim_superior = None
    while i < len(intervalos):
        if fe[i] < 5:
            lim_inferior = intervalos[i][0]
            while i < len(intervalos):
                ace = fe[i] + ace
                aco = fo[i] + aco
                if ace >= 5:
                    lim_superior = intervalos[i][1]
                    break
                else:
                    if i < len(intervalos):
                        z = i
                        pass
                i = i + 1

            if ace >= 5:
                v.append([[lim_inferior, lim_superior], aco, ace, None, None])
                lim_inferior = intervalos[i][1]

            else:
                v[len(v) - 1][0] = [lim_inferior, intervalos[len(intervalos) - 1][1]]
                v[len(v) - 1][1] = round(v[len(v) - 1][1] + aco, 4)
                v[len(v) - 1][2] = round(v[len(v) - 1][2] + ace, 4)

        else:
            v.append([intervalos[i], fo[i], round(fe[i], 4), None, None])
            lim_inferior = intervalos[i][1]

        i = i + 1
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

    calculado = v[len(v) - 1][4]
    tabulado = chi_tabulado[len(v)-1-distr]

    print("/" * 100)
    print("Valor del estadístico de prueba:", calculado)
    print("Valor tabulado para un alfa de 0,05:", tabulado)
    return tabulado >= calculado



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
    
    calculado = v[len(v) - 1][8]
    tabulado = ks_tabulado[N-1] if N <= 40 else round(1.36 / N ** 0.5, 4)

    print("/" * 100)
    print("Valor del estadístico de prueba:", calculado)
    print("Valor tabulado para un alfa de 0,05:", tabulado)
    return tabulado >= calculado