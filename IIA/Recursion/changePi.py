# Dada una cadena, calcule recursivamente (sin bucles) una nueva cadena donde todas las apariencias 
# de "pi" han sido reemplazadas por "3.14".

def change_pi(str):
    if len(str) <= 1:
        return str
    if str[:2] == "pi":
        return "3.14" + change_pi(str[2:])
    return str[0] + change_pi(str[1:])

##cadena = input("Ingresa una palabra: ")
cadena = "pipila"
print(f"Palabra cambiada: {change_pi(cadena)}")