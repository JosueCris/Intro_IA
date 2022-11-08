# Tenemos conejitos parados en una fila, numerados 1, 2, ... Los conejitos impares (1, 3, ..) 
# tienen las 2 orejas normales. Los conejitos pares (2, 4, ..) diremos que tienen 3 orejas, 
# porque cada uno tiene una patita levantada. Devuelve recursivamente el número de "orejas" en la 
# línea de conejito 1, 2, ... n (sin bucles ni multiplicación).

def bunny_ears2(bunnies):
    if(bunnies == 0):
        return 0
    if (bunnies %2) != 0:
        return 2 + bunny_ears2(bunnies-1)
    return 3 + bunny_ears2(bunnies-1)

print(f"Cantidad de orejitas: {bunny_ears2(2)}")
