# Cuente recursivamente el número total de subcadenas "abc" y "aba" que aparecen en la cadena dada.

def count_abc(str):
    if len(str) < 3:
        return 0
    if str[:3] == "abc" or str[:3] == "aba":
        return 1 + count_abc(str[2:])
    return count_abc(str[1:])

cadena = "abc"
cadena2 = "abcxxabc"
cadena3 = "abaxxaba"
print(f"Cant. abc/aba: {count_abc(cadena)}")
print(f"Cant. abc/aba: {count_abc(cadena2)}")
print(f"Cant. abc/aba: {count_abc(cadena3)}")



    