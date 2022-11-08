# Dada una matriz de ints, calcule recursivamente si la matriz contiene en algún lugar un valor 
# seguido en la matriz por ese valor multiplicado por 10. Usaremos la convención de considerar solo 
# la parte de la matriz que comienza en el índice dado. De esta manera, una llamada recursiva puede 
# pasar index+1 para moverse hacia abajo en la matriz. La llamada inicial pasará en índice como 0.

def array220(array, index):
    if len(array)-1 <= index:
        return False
    if array[index]*10 == array[index+1]:
        return True
    return array220(array, index+1)

nums1 = [1, 2, 20]
nums2 = [3, 30]
nums3 = [3]

print(array220(nums1, 0))
print(array220(nums2, 0))
print(array220(nums3, 0))
