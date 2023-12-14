# !/usr/bin/env python

import random
from time import sleep

# PARAMETROS:

bilhetes = 2
numerosPorBilhete = 9
maiorNumeroAceito = 60

#
#  NÃO ALTERAR NADA DAQUI PARA BAIXO
#


used = []

inorder = True

def geraX(x):
	global used, inorder

	ticket = []
	
	for j in range(x):
		
		if inorder:
			num = random.randint(1,maiorNumeroAceito)
			while num in used or num in ticket:
				num=random.randint(1,maiorNumeroAceito)
			used.append(num)
		else:
			num=used.pop()
			while( num in ticket ):
				num=used.pop()
		
		ticket.append(num)
		
		if len(used) == maiorNumeroAceito:
			inorder = False
			used.reverse()
			random.shuffle(used)
		elif len(used) == 0:
			inorder = True
		
		timer = random.random()
		sleep(timer/10)
	
	#print(inorder, len(used), ' - ', used)
	
	ticket.sort()
	
	return ticket

	
def main(bilhetes, numerosPorBilhete):
	global used

	numbers = []

	print('Bilhetes com {} dezenas:'.format(numerosPorBilhete))
	
	for i in range(bilhetes):

		ticket = geraX(numerosPorBilhete)
		
		if len(used) > maiorNumeroAceito:
			used = []
		
		numbers.append(ticket)

		formated_ticket = repr(ticket)

		print(i+1, formated_ticket, sep=' - ')
		# print(i+1, ' - ', '{:.2d}'.format(ticket))
		#print('{:.2d}'.format(ticket))
		
		#sleep(1)
		

main(bilhetes, numerosPorBilhete)
# main(5, 9)
# main(5, 7)
#main(2, 6) #"""

