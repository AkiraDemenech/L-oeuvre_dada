import random
#from ctypes import py_object, cast



def bytestr (d, accept = {set:	lambda o,k,v: o.add(k), 
						dict:	lambda o,k,v: o.__setitem__(k,bytestr(v)),
						list:	lambda o,k,v: o.append(k),	tuple:	None}):
	if type(d) == bytes:
		d = d.decode() 		
	if not type(d) in accept:	
		return d
	
	if type(d) == tuple:
		r = list()
	else:
		r = type(d)()	

	for p in d:		
		c = p
		if type(d) == dict:
			c = d[p]																										
		if type(p) == bytes:																					
			p = p.decode()
		accept[type(r)](r,p,c)	

	return r		
						


ALPHANUM = lambda t: t.isalnum()

class Recorte:

	def __str__ (self):
		return self.__repr__()
	
	def __repr__ (self):		 				
		return self.__class__.__name__ + '(' + self.texto.__repr__() + (",%d" %self.freq) + ((", *" + self.pref.__repr__()) * len(self.pref)) + ')'	
			


	def __hash__ (self):
		return self.texto.__hash__()

	def __init__ (self, cont, n = 1, *pre):
		self.texto = cont
		self.freq = n
		self.pref = set(pre)
		
	def __eq__ (self, outro):
		if type(self) == type(outro):
			outro = outro.texto	
		return self.texto == outro	

	def reincidir (self, prefixo = None):
		if prefixo != None:
			self.pref.add(prefixo)
		self.freq += 1
		return self.freq


class Colagem:

	def __repr__ (self):
		return "Colagem(%s)" %str(self.fonte)
		

	def __init__ (self, fonte = None, separador = ALPHANUM):
		if type(separador) == int or type(separador) == str:
			separador = ALPHANUM#cast(separador,py_object).value
		self.separ = separador
		self.fonte = set()
		if fonte == None:
			self.dicio = {}
			return

		if type(fonte) == str:
			fonte = eval(fonte)			
		self.dicio = bytestr(fonte)

	def conectar (self, origem, destino, divisor):
		g = origem.upper()
		if not g in self.dicio:
			self.dicio[g] = {None: set()}
		if not origem in self.dicio[g]:	
			self.dicio[g][origem] = {None: set()}
		if not divisor in self.dicio[g][origem]: 	
			self.dicio[g][origem][divisor] = set()
		if destino in self.dicio[g][origem][divisor]:	
			for d in self.dicio[g][origem][divisor]:
				if d == destino:
					d.reincidir()
					break
		else:	
			self.dicio[g][origem][divisor].add(Recorte(destino))

		if destino in self.dicio[g][origem][None]:	
			for d in self.dicio[g][origem][None]:
				if d == destino:
					d.reincidir(divisor)
					break
		else: 
			self.dicio[g][origem][None].add(Recorte(destino,pre=divisor)) 	

		if destino in self.dicio[g][None]:	
			for d in self.dicio[g][None]:
				if d == destino:
					d.reincidir(divisor)
					break
		else: 
			self.dicio[g][None].add(Recorte(destino, pre = divisor)) 	




	def adicionar (self, texto):	
		self.fonte.add(texto)
		p = s = ''
		for char in texto:
			if self.separ(char):
				if len(s):
					pass

				p += char
			else: 	
				s += char
		

		

				

			

