from Tree import Tree

##  MAIN
# raiz = Tree(55)
# raiz.add(27)
# # raiz.add(32)
# # raiz.add(64)
# raiz.add(57)
# raiz.add(59)
# raiz.add(77)
# # raiz = Tree(50)
# # raiz.add(25)
# # raiz.add(10)
# # raiz.add(70)
# # raiz.add(8)


# ##  IMPRESIONES
# print("PRE-ORDEN")
# raiz.pre_orden()
# print("\n")

# print("IN-ORDEN")
# raiz.in_orden()
# print("\n")

# print("POST-ORDEN")
# raiz.post_orden()
# print("\n")


# ##  BUSQUEDAS
# nodo = raiz.search(55)
# if not nodo:
#     print("No existe")
# else:
#     print(f"Encontrado: {nodo.data}")
    
# nodo = raiz.search(24)
# if not nodo:
#     print("No existe")
# else:
#     print(f"Encontrado: {nodo.data}")


# ##  CALCULO DE VALORES
# nodos = raiz.nodes_cant()
# hojas = raiz.leafs_cant()
# altura = raiz.height()
# factor = raiz.balance_factor()
# print(f"Cantidad de nodos: {nodos}")
# print(f"Cantidad de hojas: {hojas}")
# print(f"Altura del arbol: {altura}")
# print(f"Factor de equilibrio: {factor}")

# print(f"El mas a la derecha del lado izquierdo: {raiz.left.rightmost().data}")
# print(f"El mas a la derecha del lado derecho: {raiz.right.rightmost().data}")
# print(f"El mas a la izquierda del lado izquierdo: {raiz.left.leftmost().data}")
# print(f"El mas a la izquierda del lado derecho: {raiz.right.leftmost().data}")

# # raiz = raiz.balance_tree()

# ##  CALCULO DE VALORES DESPUÉS DE LA ROTACIÓN
# nodos = raiz.nodes_cant()
# hojas = raiz.leafs_cant()
# altura = raiz.height()
# factor = raiz.balance_factor()
# print(f"\nCantidad de nodos: {nodos}")
# print(f"Cantidad de hojas: {hojas}")
# print(f"Altura del arbol: {altura}")
# print(f"Factor de equilibrio: {factor}")

# print(f"El mas a la derecha del lado izquierdo: {raiz.left.rightmost().data}")
# print(f"El mas a la derecha del lado derecho: {raiz.right.rightmost().data}")
# print(f"El mas a la izquierda del lado izquierdo: {raiz.left.leftmost().data}")
# print(f"El mas a la izquierda del lado derecho: {raiz.right.leftmost().data}")



## MENU INTERACTIVO PARA EL USUARIO QUE DESEE MANEJAR EL ARBOL
raiz = None
op = 9

while op != 0:
    print("Selecciona una opcion para el arbol binario de busqueda - AVL:")
    op = int(input("\t[1]: Insertar\n\t[2]: Pre-Orden\n\t[3]: In-Orden\n\t[4]: Post-Orden\n\t[5]: Buscar\n\t[6]: Eliminar\n\t[7]: Datos\n\t[0]: Salir\n> "))

    if op == 1:
        num = int(input("Ingresa un numero en el arbol: "))
        if not raiz:
            raiz = Tree(num)
        else:
            raiz.add(num)
    if op == 2:
        print("PRE-ORDEN")
        raiz.pre_orden()
        print("\n")
    if op == 3:
        print("IN-ORDEN")
        raiz.in_orden()
        print("\n")
    if op == 4:
        print("POST-ORDEN")
        raiz.post_orden()
        print("\n")
    if op == 5:
        num = int(input("Ingresa el numero a buscar: "))
        nodo = raiz.search(num)
        if not nodo:
            print("No existe \n")
        else:
            print(f"Encontrado: {nodo.data} \n")
    if op == 6:
        num = int(input("Ingresa el numero a eliminar: "))
        raiz = raiz.delete(num)
    if op == 7:
        nodos = raiz.nodes_cant()
        hojas = raiz.leafs_cant()
        altura = raiz.height()
        factor = raiz.balance_factor()
        print(f"Cantidad de nodos: {nodos}")
        print(f"Cantidad de hojas: {hojas}")
        print(f"Altura del arbol: {altura}")
        print(f"Factor de equilibrio: {factor}")
print("Vuelva pronto :)")