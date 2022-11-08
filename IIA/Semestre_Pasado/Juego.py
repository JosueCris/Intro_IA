class Personaje(object): ## Si es object la clase heredada no hace falta indicarlo
	def __init__(self, nombre, vitalidad, fuerza):
		super(Personaje, self).__init__()
		self.nombre = nombre
		self.vitalidad = vitalidad
		self.fuerza = fuerza

	def caminar(self):
		pass

	def atacar(self):
		pass	

	def imprime_nombre(self):
		print(self.nombre)	


class Duelista(Personaje):
	def __init__(self, nombre, vitalidad, fuerza, sigilo, invisible):
		super(Duelista, self).__init__(nombre, vitalidad, fuerza)
		self.sigilo = sigilo
		self.invisible = invisible

	def mueve_con_sigilo(self):
		self.sigilo = True
		self.caminar()	


class Centinela(Personaje):
	def __init__(self, nombre, vitalidad, fuerza):
		super(Centinela, self).__init__(nombre, vitalidad, fuerza)
		self.arg = arg


class Controlador(Personaje):
	def __init__(self, nombre, vitalidad, fuerza):
		super(Duelista, self).__init__(nombre, vitalidad, fuerza)
		self.arg = arg
						
						
						
'''
Rafa = Personaje("Rafa", 100, 50)
Juan = Personaje("Juan", 100, 10)
Ricardo = Personaje("Ricardo", 100, 15)
'''
'''
print(Rafa.nombre)
print(Ricardo.nombre)
print(Juan.nombre)	
'''

characters = [Personaje("Rafa", 100, 50),
			  Duelista("Juan", True, False),
			  Personaje("Ricardo", 100, 15)]

for char in characters:
	char.imprime_nombre()	

##imprime_nombre(characters[0]) ## Es metodo de clase, NO FUNCION
characters[0].imprime_nombre() ## Escribirlo de esta forma si sirve			  