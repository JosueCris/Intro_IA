from pty import slave_open
from Tree import Tree

##  MAIN
# raiz = Tree(55)
# raiz.add(27)
# raiz.add(32)
# raiz.add(64)
# raiz.add(59)
# raiz.add(77)
raiz = Tree(50)
raiz.add(25)
raiz.add(10)


##  IMPRESIONES
print("PRE-ORDEN")
raiz.pre_orden()
print("\n")

print("IN-ORDEN")
raiz.in_orden()
print("\n")

print("POST-ORDEN")
raiz.post_orden()
print("\n")


##  BUSQUEDAS
nodo = raiz.search(55)
if not nodo:
    print("No existe")
else:
    print(f"Encontrado: {nodo.data}")
    
nodo = raiz.search(24)
if not nodo:
    print("No existe")
else:
    print(f"Encontrado: {nodo.data}")


##  CALCULO DE VALORES
nodos = raiz.nodes_cant()
hojas = raiz.leafs_cant()
altura = raiz.height()
factor = raiz.balance_factor()
print(f"Cantidad de nodos: {nodos}")
print(f"Cantidad de hojas: {hojas}")
print(f"Altura del arbol: {altura}")
print(f"Factor de equilibrio: {factor}")


print(f"El mas a la derecha del lado izquierdo: {raiz.left.more_to_right().data}")
print(f"El mas a la derecha del lado derecho: {raiz.right.more_to_right().data}")
print(f"El mas a la izquierda del lado izquierdo: {raiz.left.more_to_left().data}")
print(f"El mas a la izquierda del lado derecho: {raiz.right.more_to_left().data}")

raiz.lsr()

print(f"\nCantidad de nodos: {nodos}")
print(f"Cantidad de hojas: {hojas}")
print(f"Altura del arbol: {altura}")
print(f"Factor de equilibrio: {factor}")


## MENU INTERACTIVO PARA EL USUARIO QUE DESEE MANEJAR EL ARBOL
# raiz = None
# op = 9

# while op != 0:
#     print("Selecciona una opcion para el arbol binario de busqueda:")
#     op = int(input("\t[1]: Insertar\n\t[2]: Pre-Orden\n\t[3]: In-Orden\n\t[4]: Post-Orden\n\t[5]: Buscar\n\t[6]: Eliminar\n\t[7]: Cant. Nodos\n\t[8]: Cant. Hojas\n\t[9]: Altura\n\t[10]: Fact. Equilibrio\n\t[0]: Salir\n> "))

#     if op == 1:
#         num = int(input("Ingresa un numero en el arbol: "))
#         if not raiz:
#             raiz = Tree(num)
#         else:
#             raiz.add(num)
#     if op == 2:
#         print("PRE-ORDEN")
#         raiz.pre_orden()
#         print("\n")
#     if op == 3:
#         print("IN-ORDEN")
#         raiz.in_orden()
#         print("\n")
#     if op == 4:
#         print("POST-ORDEN")
#         raiz.post_orden()
#         print("\n")
#     if op == 5:
#         num = int(input("Ingresa el numero a buscar: "))
#         nodo = raiz.search(num)
#         if not nodo:
#             print("No existe \n")
#         else:
#             print(f"Encontrado: {nodo.data} \n")
#     if op == 6:
#         num = int(input("Ingresa el numero a eliminar: "))
#         raiz.delete(num)
#     if op == 7:
#         nodos = raiz.nodes_cant()
#         print(f"Cantidad de nodos: {nodos} \n")
#     if op == 8:
#         hojas = raiz.leafs_cant()
#         print(f"Cantidad de hojas: {hojas} \n")
#     if op == 9:
#         altura = raiz.height()
#         print(f"Altura del arbol: {altura} \n")
#     if op == 10:
#         factor = raiz.balance_factor
#         print(f"Factor de equilibrio: {factor} \n")

# print("Vuelva pronto :)")