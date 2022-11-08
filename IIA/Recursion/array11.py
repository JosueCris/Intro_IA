# Dada una matriz de ints, calcule recursivamente el número de veces que el valor 11 aparece en la matriz.
# Usaremos la convención de considerar solo la parte de la matriz que comienza en el índice dado.
# De esta manera, una llamada recursiva puede pasar index+1 para moverse hacia abajo en la matriz.
# La llamada inicial pasará en índice como 0.

def array11(array, index):
    if len(array) <= index:
        return 0
    if array[index] == 11:
        return 1 + array11(array, index+1)
    return array11(array, index+1)

numeros = [11, 9, 11, 14, 11]
print(f"Cantidad de onces: {array11(numeros, 0)}")