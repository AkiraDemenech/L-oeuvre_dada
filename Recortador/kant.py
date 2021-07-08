import Colador

k = Colador.Colagem()
for a in {'intro.txt','cont.txt'}:
	k.adicionar(open('kant/' + a,'r',encoding='utf-8').read())

f = open('kant.txt','w',encoding='utf-8')
s = k.marca
while True:
	c = None
	while c == None:
		c = Colador.sortear(k.dicio[s.upper()][s])
	s = Colador.sortear(k.dicio[s.upper()][s][c]).texto
	print(c + s,file=f,end='')
	if s == k.marca:
		break
