#!/usr/bin/env python

import random

def lotterytickts(numtix):
	listoftix = []  #list of all tickets generated
	for i in range(numtix):
		a = random.randint(1,60)
		b = random.randint(1,60)
		c = random.randint(1,60)
		d = random.randint(1,60)
		e = random.randint(1,60)
		f = random.randint(1,60)
		ticket = [a,b,c,d,e,f]
		ticket.sort()							  #smallest to largest
		ticket.append(random.randint(1,60))		#megaball
		listoftix.append(ticket)				   #megaball number at the end at position ticket[5]
	return listoftix

def checktix(tix):
	winning = []								   #list of all winning tickets
	a = random.randint(1,60)
	b = random.randint(1,60)
	c = random.randint(1,60)
	d = random.randint(1,60)
	e = random.randint(1,60)
	f = random.randint(1,60)
	winner = [a,b,c,d,e,f]
	winner.sort()
	winner.append(random.randint(1,46))			#jackpot megaball
	print ("$$: " + str(winner))					 #jackpot numbers
	for x in tix:								  #one ticket from the list of tickets
		if x == winner:							#JACKPOT!
			winning.append("MegaMillion!!!: " + str(x))
			break
		if x[0:4] == winner[0:4]:				  #WIN $250K
			winning.append("$250,000!: " + str(x))
			break
		match = 0								  #num of matching numbers
		for i in x[0:4]:
			if i in winner[0:4]:
				match += 1
		if match == 4 and x[5] == winner[5]:	   #WIN $10K
			winning.append("$10,000: " + str(x))
			break
		if match == 4:							 #WIN $150
			winning.append("$150: " + str(x))
			break
		if match == 3 and x[5] == winner[5]:	   #WIN $150
			winning.append("$150: " + str(x))
			break
		if match == 2 and x[5] == winner[5]:	   #WIN $10
			winning.append("$10: " + str(x))
			break
		if match == 3:							 #WIN $7
			winning.append("$7: " + str(x))
			break
		if match == 1 and x[5] == winner[5]:	   #WIN $3
			winning.append("$3: " + str(x))
			break
		if match == 0 and x[5] == winner[5]:	   #WIN $2
			winning.append("$2: " + str(x))
	return winning								 #return list of winning tickets

a = lotterytickts(10) #arg is					# of tickets purchased. generates random #'d tickets.
print (checktix(a))								#this function generates a winner and checks all your tickets.

