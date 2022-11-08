# Dada una cadena, calcule recursivamente una nueva cadena donde todos los caracteres 'x' minúsculas 
# se hayan movido al final de la cadena.

def end_x(str):
    if len(str) < 2:
        return str
    if str[0] == 'x':
        return end_x(str[1:]) + 'x'
    return str[0] + end_x(str[1:])

cad1 = "xxre"
cad2 = "xxhixx"
cad3 = "xhixhix"

print(f"Palabra modificada: {end_x(cad1)}")
print(f"Palabra modificada: {end_x(cad2)}")
print(f"Palabra modificada: {end_x(cad3)}")