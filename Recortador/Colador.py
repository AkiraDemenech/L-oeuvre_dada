import random

SIMPLES = lambda x: True
JUSTO = lambda p: p.freq


def sortear (c,alt = {tuple,list,dict},rand=random.randint):
	peso = SIMPLES
	l = len(c)
	if type(c) in alt:
		if type(c) == dict:
		#	print('Sorteando chave de dicionário')
			return sortear(c.keys())
	#	print('Sorteando item com peso')	
		l = c[1]
		c = c[0]
		peso = JUSTO				
	if l <= 0:
	#	print('sem tamanho')
		return 
	l = rand(0,l - 1)		
	for t in c:	
		if l < peso(t):
			break
		l -= peso(t)
	return t	





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
		return self.__class__.__name__ + '(' + self.texto.__repr__() + (",%d" %self.freq) + ((", " + self.pref.__repr__()) * (len(self.pref) >= 1)) + ')'	
			


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
	if type(conjunto) != set:
		conjunto[1] += 1
		conjunto = conjunto[0]
	if termo in conjunto:
		for c in conjunto:
			if c == termo:
				return c.reincidir(inter)				
	conjunto.add(Recorte(termo,pre=inter))			
	return True

class Colagem:

	def __repr__ (self):
		return self.__str__()
	def __str__ (self):
		return "Colagem(%s,%s)" %(str(self.dicio),self.marca.__repr__())
		

	def __init__ (self, fonte = None, marcador = '', separador = ALPHANUM):

		self.marca = marcador
		self.separ = separador
		self.fonte = set()
		if fonte == None:
			self.dicio = {}
			return

		while type(fonte) == str:
			fonte = eval(fonte)			
			if type(fonte) == bytes:	
				fonte = fonte.decode()
		self.dicio = bytestr(fonte)

	def conectar (self, origem, destino, divisor):
		g = origem.upper()
		if not g in self.dicio:
			self.dicio[g] = {None: [set(), False]}
		if not origem in self.dicio[g]:	
			self.dicio[g][origem] = {None:[set(),False]}
		if not divisor in self.dicio[g][origem]: 	
			self.dicio[g][origem][divisor] = [set(),0]
		incidir(self.dicio[g][origem][divisor], destino)	
			

		incidir(self.dicio[g][origem][None], destino,divisor) 	
		incidir(self.dicio[g][None],destino,divisor)	
	#	print(origem.__repr__(), divisor.__repr__(), destino.__repr__())




	def adicionar (self, texto, vazio = None, separar = None):	
		if type(texto) != str:
			for t in texto:
				self.adicionar(t,vazio,separar)
				
			return
		if len(texto) <= 0:
			return
		if vazio == None:
			vazio = self.marca	
		if separar == None:
			separar = self.separ
		self.fonte.add(texto)
		o = None
		p = s = vazio
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
		if separar(char):		
			self.conectar(o, p, s)
			s = vazio
		self.conectar(p,vazio, s)	
			

		

		

				


def teste ():			
	'''
	a = Colagem()
	a.adicionar('\r   , \t ,--\nhg')#,separar=NOTWHITE)
	print(a)
	c = a.marca
	while True:
		print(repr(c))
		for c in a.dicio[c.upper()][None][0]:
			print(c)
			c = c.texto
			if len(c):
				break
		if c == a.marca:
			if input('Terminou de testar já?').lower()[0] != 'n':
				break

	b = eval(open('teste.log','r').read()).decode().replace('}},','}},\n\t')
	print(b,file=open('teste.txt','w',encoding='utf8'))
	a = Colagem(b)'''
	a = Colagem()
	a.adicionar(open('../Geral.java','r').read())
	a.adicionar(open('../Quadra/Hexa.java','r').read())
	a.adicionar(open('../Bingo/Bingo.java','r').read())
	f = open('resultado.java','w')
	b = ''
	while True:
		c = None
		while c == None:
			c = sortear(a.dicio[b.upper()][b])
		b = sortear(a.dicio[b.upper()][b][c]).texto
		print(c + b,file=f,end='')
		if len(b):
			continue
		f.close()
		break
		
if '__main__' == __name__:
	teste()		