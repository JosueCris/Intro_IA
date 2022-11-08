# Dada una cadena, calcule recursivamente (sin bucles) el número de subcadenas "11" en la cadena. 
# Las subcadenas "11" no deben superponerse.

def count11(str):
    if len(str) < 2:
        return 0
    if str[:2] == "11":
        return 1 + count11(str[2:])
    return count11(str[1:])

cad1 = "11abc11"
cad2 = "abc11x11x11"
cad3 = "111"

print(f"Cantidad de onces: {count11(cad1)}")
print(f"Cantidad de onces: {count11(cad2)}")
print(f"Cantidad de onces: {count11(cad3)}")