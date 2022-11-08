# Dada una cadena, calcule recursivamente una nueva cadena donde los caracteres idénticos que son 
# adyacentes en la cadena original están separados entre sí por un "*".

def pair_star(str):
    if len(str) < 2:
        return str
    if str[0] == str[1]:
        return str[0] + '*' + pair_star(str[1:])
    return str[0] + pair_star(str[1:])

cadena = "hello"
cadena2 = "xxyy"
cadena3 = "aaaa"
print(f"Palabra: {pair_star(cadena)}")
print(f"Palabra: {pair_star(cadena2)}")
print(f"Palabra: {pair_star(cadena3)}")