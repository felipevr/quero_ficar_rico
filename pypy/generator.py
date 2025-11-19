#!/usr/bin/env python

import random
from time import sleep


# PARAMETROS:

bilhetes = 12

# JOGOS:
jogo = 'lotofacil2'  # 'lotofacil1', 'lotofacil2', 'megasena', 'megasena7', 'megasena8', 'quina'


def configurarNumerosLoteria(jogo):
	global bilhetes, numerosPorBilhete, maiorNumeroAceito
	if jogo == 'lotofacil1':
		numerosPorBilhete = 15
		maiorNumeroAceito = 25
	elif jogo == 'lotofacil2':
		numerosPorBilhete = 16
		maiorNumeroAceito = 25
	elif jogo == 'megasena':
		numerosPorBilhete = 6
		maiorNumeroAceito = 60
	elif jogo == 'megasena7':
		numerosPorBilhete = 7
		maiorNumeroAceito = 60
	elif jogo == 'megasena8':
		numerosPorBilhete = 8
		maiorNumeroAceito = 60
	elif jogo == 'quina':
		numerosPorBilhete = 5
		maiorNumeroAceito = 80



#
#  NÃO ALTERAR NADA DAQUI PARA BAIXO
#

numerosPorBilhete = 1
maiorNumeroAceito = 1

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

# Configurar os números de loteria de acordo com o jogo
configurarNumerosLoteria(jogo)		

main(bilhetes, numerosPorBilhete)
# main(5, 9)
# main(5, 7)
#main(2, 6) #"""

