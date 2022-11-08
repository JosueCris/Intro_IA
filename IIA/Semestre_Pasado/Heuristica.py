def distancia(pos1, pos2):
	return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1]) 

def heuristica(matriz, pos_dic):
	suma = 0
##	print(matriz)
	for x in range(len(matriz[0])):
		for y in range(len(matriz)):
			suma = suma + distancia([x, y], pos_dic[matriz[x][y]])

	return suma

def calcula_diccionario(meta):
	dic = {}
	for x in range(len(meta[0])):
		for y in range(len(meta)):
			dic[meta[x][y]] = [x, y]
	return dic
			

mat = [
				[1,   2,    3],
				[8,  "_",   7],
				[6,   4,    5] 
]



hijo1 = [
				[1,  "_",   3],
				[8,   2,    7],
				[6,   4,    5]
]

hijo2 = [ 
				[1,   2,    3],
				[8,   4,    7],
				[6,  "_",   5] 
]		

hijo3 = [ 
				[1,   2,    3],
				["_", 8,    7],
				[6,   4,    5] 
]

hijo4 = [ 
				[1,   2,    3],
				[8,   7,  "_"],
				[6,   4,    5] 
]		  		    


meta = [ 
				[1,   2,    3],
				[4,   5,    6],
				[7,   8,  "_"] 
]

##h = heuristica(mat, calcula_diccionario(meta))

diccionario = calcula_diccionario(meta)

print(diccionario)
h = heuristica(mat, diccionario)
h1 = heuristica(hijo1, diccionario)
h2 = heuristica(hijo2, diccionario)
h3 = heuristica(hijo3, diccionario)
h4 = heuristica(hijo4, diccionario)

print(h)
print(h1)
print(h2)
print(h3)
print(h4)