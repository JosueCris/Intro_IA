# Tenemos un número de conejitos y cada conejito tiene dos grandes orejas flojas. 
# Queremos calcular el número total de orejas en todos los conejos de forma recursiva 
# (sin bucles ni multiplicación).

def bunny_ears(bunnies):
    if bunnies == 0:
        return 0
    return 2 + bunny_ears(bunnies-1)

print(f"Cantidad de orejas: {bunny_ears(0)}")
print(f"Cantidad de orejas: {bunny_ears(1)}")
print(f"Cantidad de orejas: {bunny_ears(2)}")