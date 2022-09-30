#!/usr/bin/env python

import random
from time import sleep

# PARAMETROS:

bilhetes = 15
numerosPorBilhete = 7

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
			num = random.randint(1,60)
			while num in used or num in ticket:
				num=random.randint(1,60)
			used.append(num)
		else:
			num=used.pop()
			while( num in ticket ):
				num=used.pop()
		
		ticket.append(num)
		
		if len(used) == 60:
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
	
	for i in range(bilhetes):

		ticket = geraX(numerosPorBilhete)
		
		if len(used) > 60:
			used = []
		
		numbers.append(ticket)
		
		print(i+1, ' - ', ticket, ' x ', numerosPorBilhete)
		
		#sleep(1)
		

#main(bilhetes, numerosPorBilhete)
main(9, 8)
main(2, 7)
#main(2, 6) #"""
