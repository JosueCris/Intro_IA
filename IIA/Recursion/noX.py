# Dada una cadena, calcule recursivamente una nueva cadena donde se hayan eliminado todos los caracteres 'x'.

def no_x(str):
    if len(str) < 1:
        return str
    if str[0] == 'x':
        return no_x(str[1:])
    return str[0] + no_x(str[1:])

cadena = "xaxb"
cadena2 = "abc"
cadena3 = "xx"

print(f"{cadena} sin x: {no_x(cadena)}")
print(f"{cadena2} sin x: {no_x(cadena2)}")
print(f"{cadena3} sin x: {no_x(cadena3)}")