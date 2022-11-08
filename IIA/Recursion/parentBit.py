# Dada una cadena que contiene un solo par de paréntesis, calcule recursivamente una nueva cadena 
# hecha solo del paréntesis y su contenido, por lo que "xyz(abc)123" produce "(abc)".

def parent_bit(str):
    if str[0]=='(' and str[len(str)-1]==')':
        return str
    if(str[0] == '('):
        return parent_bit(str[0:len(str)-1])
    if str[len(str)-1] == ')':
        return parent_bit(str[1:])
    return parent_bit(str[1:len(str)-1])
    
cad1 = "xyz(abc)123"
cad2 = "x(hello)"
cad3 = "(xy)1"

print(f"Palabra recortada: {parent_bit(cad1)}")
print(f"Palabra recortada: {parent_bit(cad2)}")
print(f"Palabra recortada: {parent_bit(cad3)}")