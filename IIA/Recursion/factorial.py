# Dado n de 1 o más, devuelva el factorial de n, que es n * (n-1) * (n-2) ... 1. 
# Calcule el resultado recursivamente (sin bucles).

def factorial(n):
    if n == 0:
        return 1
    return (n * factorial(n-1))

num = int(input("Ingresa un numero: "))
print(f"El factorial de {num} es: {factorial(num)}")