# Dada una cadena, calcule recursivamente (sin bucles) el número de veces que aparece "hi" minúscula 
# en la cadena.

def count_hi(str):
    if len(str) < 2:
        return 0
    if str[:2] == "hi":
        return 1 + count_hi(str[2:])
    return count_hi(str[1:])

cadena = "xxhixx"
cadena2 = "xhixhix"
cadena3 = "hi"

print(f"Cantidad de hi: {count_hi(cadena)}")
print(f"Cantidad de hi: {count_hi(cadena2)}")
print(f"Cantidad de hi: {count_hi(cadena3)}")