import random

def dadapo (versos, vocabu = None, prefixo = '', sep = ' ', tab = True, max = 1, esc = 0):
	if vocabu == None:
		vocabu = palavras(versos)
		
	if versos.__class__ == str:
		versos = versos.splitlines()

	try:
		ddp = []
		while max > 0:
			max -= 1	
			c = len(versos)
			ddp.clear()
			while c > 0:
				c += -1
				ln = prefixo
				if tab:
					d = 0
					while d < len(versos[c]):
						if not versos[c][d].isspace():
							ln += versos[c][:d]
							break
						d += 1#versos[c][d].isspace()
				while len(ln) < len(versos[c]):
					ln += vocabu[int(random.random()*len(vocabu))] + sep
				ddp.insert(0,ln)
			vocabu.clear()
			vocabu = palavras(ddp,vocabu)
			if esc > random.random():
		#		print('Fim prematuro')
				break
		#	print(max)
	except KeyboardInterrupt:
		print('\nRetornando resultado atual')
	return ddp
	
def palavras (fonte, res = None):
	if fonte.__class__ == str:
		return fonte.split()
	
	if res == None:
		res = []
		
	for s in fonte:
		res.extend(palavras(s))
	return res