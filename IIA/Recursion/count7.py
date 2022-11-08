# Dado un int n no negativo, devuelva el recuento de las ocurrencias de 7 como un dígito, 
# por lo que, por ejemplo, 717 produce 2. (sin bucles). Tenga en cuenta que mod (%) por 10 produce 
# el dígito más a la derecha (126 % 10 es 6), mientras que dividir (/) por 10 elimina el dígito más 
# a la derecha (126 / 10 es 12).

def count7(n):
    if n == 0:
        return 0
    if n % 10 == 7:
        return 1 + count7(n/10)
##    print(n)
    return count7(n/10)

num = int(input("Ingresa un numero: "))
print(f"Cantidad de sietes: {count7(num)}")