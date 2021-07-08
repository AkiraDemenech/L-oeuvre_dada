import random



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
NOTWHITE = lambda t: t.isprintable() and not t.isspace()

class Recorte:

	def __str__ (self):
		return self.__repr__()
	
	def __repr__ (self):		 				
		return self.__class__.__name__ + '(' + self.texto.__repr__() + (",%d" %self.freq) + ((", " + self.pref.__repr__()) * len(self.pref)) + ')'	
			


	def __hash__ (self):
		return self.texto.__hash__()

	def __init__ (self, cont, n = 1, pre = ''):
		self.texto = cont
		self.freq = n
		if type(pre) != set:
			if pre == None:
				pre = set()
			else:
				pre = {pre}
		self.pref = pre
		
		
	def __eq__ (self, outro):
		if type(self) == type(outro):
			outro = outro.texto	
		return self.texto == outro	

	def reincidir (self, prefixo = None):
		if prefixo != None:
			self.pref.add(prefixo)
		self.freq += 1
		return self.freq

def incidir (conjunto, termo, inter = None):				
	if termo in conjunto:
		for c in conjunto:
			if c == termo:
				return c.reincidir(inter)				
	conjunto.add(Recorte(termo,pre=inter))			
	return True

class Colagem:

	def __repr__ (self):
		return "Colagem(%s)" %str(self.fonte)
		

	def __init__ (self, fonte = None, separador = ALPHANUM):
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
		incidir(self.dicio[g][origem][divisor], destino)	
			

		incidir(self.dicio[g][origem][None], destino,divisor) 	
		incidir(self.dicio[g][None],destino,divisor)	


	def adicionar (self, texto, vazio = '', separar = None):	
		if separar == None:
			separar = self.separ
		self.fonte.add(texto)
		p = o = s = vazio
		for char in texto:
			if separar(char):
				if o == None:
					o = p					
					p = vazio
				p += char
			else: 	
				if o != None: 
					self.conectar(o,p,s)					
					s = vazio					
					o = None
				s += char

		

		

				


			

