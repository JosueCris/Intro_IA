# Dada una cadena, calcule recursivamente el número de veces que aparece "hi" minúscula en la cadena,
# sin embargo, no cuente "hi" que tienen una 'x' inmedamente antes de ellos.

def count_hi2(str):
    if(len(str) < 2):
        return 0
    if str[:2] == "hi":
        return 1 + count_hi2(str[2:])
    if len(str)>2 and str[:3]=="xhi":
        return count_hi2(str[3:])
    return count_hi2(str[1:])

print(f"Cantidad de hi: {count_hi2('ahixhi')}")
print(f"Cantidad de hi: {count_hi2('ahibhi')}")
print(f"Cantidad de hi: {count_hi2('xhixhi')}")