import random

def dadapo (versos, vocabu = None, prefixo = '', sep = ' ', tab = True):
	if vocabu == None:
		vocabu = palavras(versos)

	if versos.__class__ == str:
		versos = versos.splitlines()

	ddp = []
	c = len(versos)
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
	return ddp
	
def palavras (fonte):
	if fonte.__class__ == str:
		return fonte.split()
		
	res = []
	for s in fonte:
		res.extend(palavras(s))
	return res