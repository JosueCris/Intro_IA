# Dada una cadena y una subcadena no vacía, calcule recursivamente si al menos n copias de sub aparecen 
# en la cadena en algún lugar, posiblemente con superposición. N no será negativo.

from re import sub


def str_copies(str, sub, n):
    if n == 0:
        return True
    if len(str) < len(sub):
        return False
    if sub == str[:len(sub)]:
        return 1 + str_copies(str_copies(str[len(sub):], sub, n-1))
    return str_copies(str_copies(str[1:], sub, n))

cad = "catcowcat"
sub1 = "cat"
sub2 = "cow"

print(f"Numero de subs: {str_copies(cad, sub1, 2)}")
print(f"Numero de subs: {str_copies(cad, sub2, 2)}")
print(f"Numero de subs: {str_copies(cad, sub1, 2)}")