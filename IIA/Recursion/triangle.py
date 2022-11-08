# Tenemos triángulo hecho de bloques. La fila superior tiene 1 bloque, la siguiente fila hacia abajo 
# tiene 2 bloques, la siguiente fila tiene 3 bloques, y así sucesivamente. Calcular recursivamente 
# (sin bucles ni multiplicación) el número total de bloques en dicho triángulo con el número dado de filas.

def triangle(rows):
    if rows == 0:
        return 0
    return rows + triangle(rows-1)

print(f"Cantidad de bloques: {triangle(0)}")
print(f"Cantidad de bloques: {triangle(1)}")
print(f"Cantidad de bloques: {triangle(2)}")
