# Dada una cadena, calcule recursivamente (sin bucles) el número de caracteres 'x' minúsculas en la cadena.

def count_x(str):
    if(len(str) == 0):
        return 0
    if str[0] == 'x':
        return 1 + count_x(str[1:])
    return count_x(str[1:])

cadena = "Xalaxacaxar"
print(f"Cantidad de equis: {count_x(cadena)}")