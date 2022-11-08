# Dada una cadena y una subcadena no vacía, calcule recursivamente el número de veces que 
# aparece esa sub en la cadena, sin que las subcadenas se superpongan.

def str_count(str, sub):
    if len(str) < len(sub):
        return 0
    if sub == str[:len(sub)]:
        return 1 + str_count(str[len(sub):], sub)
    return str_count(str[1:], sub)

cadena = "catcowcat"

sub = "cat"
sub2 = "cow"
sub3 = "dog"

print(f"Cant. de {sub} en {cadena}: {str_count(cadena, sub)}")
print(f"Cant. de {sub2} en {cadena}: {str_count(cadena, sub2)}")
print(f"Cant. de {sub3} en {cadena}: {str_count(cadena, sub3)}")
