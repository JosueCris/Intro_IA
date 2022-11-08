class Diapason(object):
	def __init__(self):
##		super(Diapason, self).__init__()
		self.trastes = 25

class Guitarra:
	def __init__(self, cue, cuer, mat):
		self.diapason = Diapason()
		self.cuerpo = cue
		self.cuerdas = cuer
		self.MaterialCuerdas = mat

	def propiedades(self):
		print(f"cuerpo: {self.cuerpo}")
		print(f"cuerdas: {self.cuerdas}")
		print(f"material de cuerdas: {self.MaterialCuerdas}")
		print(f"trastes: {self.diapason.trastes}")

	def suena(self, acorde):
		if acorde == "la":
			print("piiing")


class Electrica(Guitarra):
##	def __init__(self, cue, cuer, mat, past=1, PalancadeVibrato=1):
##		super(Electrica, self).__init__(cue, cuer, mat)
	def __init__(self, past=1, PalancadeVibrato=1):
		super(Electrica, self).__init__("solido o semisolido", 6, "metalica")
		self.past = past
		self.PalancadeVibrato = PalancadeVibrato

	def propiedades(self):
		Guitarra.propiedades(self)
		print(f"pasta: {self.past}")
		print(f"vibrato: {self.PalancadeVibrato}")

	def amplifica(self, nota):
		self.suena(nota)
		print("* Amplificando electricamente *")


class Acustica(Guitarra):
	def __init__(self, caja=1, cue="hueco", cuer=6, mat="nylon"):
		super(Acustica, self).__init__(cue, cuer, mat)
		self.cajaDeResonancia = caja
		self.cuerpo = cue
		self.cuerdas = cuer
		self.MarerialCuerdas = mat
		self.diapason = Diapason()
	
	def propiedades(self):
		Guitarra.propiedades(self)
		print(f"Caja de resonancia: {self.cajaDeResonancia}")

	def amplifica(self, nota):
		self.suena(nota)
		print("* Amplificando acusticamente *")

def imprime(lista):
	for guitarras in lista:
		guitarras.propiedades()
		print("------------------------------")




## MAIN
gui = Electrica(2, 4)
##gui.propiedades()
##gui.amplifica("la")

acu = Acustica()
##acu.propiedades()
##acu.amplifica("la")
acu.cuerdas = 9
acu.diapason.trastes = 30
##acu.propiedades()

milista = []
milista.append(acu)
milista.append(Electrica())
milista[0].propiedades()
milista[0].amplifica("la")

print("\n\nLista de Guitarras:")
imprime(milista)




'''
# Instancias de guitarra
guit1 = Guitarra("madera de pino", 6, "nylon")
guit2 = Guitarra("madera cualquiera", 6, "metal")
guit3 = Guitarra("madera de arce", 6, "metal")

# Los agregamos a una lista
lista = [guit1, guit2, guit3]

print("Lista de guitarras normales")
# Recorremos la lista con el for-each
imprime(lista)

# Instancias de electrica
elect1 = Electrica("metal", 6, "metal")
elect2 = Electrica("aluminio", 6, "nylon")

# Agregamos las electricas con append() a la lista
lista.append(elect1);
lista.append(elect2);

print("\n\nLista de guitarras normales con electricas")
# Volvemos a recorrer la lista con los nuevos objetos
imprime(lista)
'''



		