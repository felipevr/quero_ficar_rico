# -*- coding: utf-8 -*- """ Created on Tue Aug 20 17:23:37 2013 @author: Paddy McCarthy """ 
try: # Python 2/3 compatibility 
	raw_input 
except:
	raw_input = input
import readline

prev = ": '!!'"
print('$ ' + prev)
while True:
	cmd = raw_input('$ ').rstrip()
	dquote = squote = skipnext = False
	result = []
	for this, nxt in zip(cmd, cmd[1:] + ' '):
		if skipnext:
			skipnext = False
			continue
		elif this == '"' and not squote:
			dquote = not dquote
			result.append(this)
		elif this == "'" and not dquote:
			squote = not squote
			result.append(this)
		elif this == '!' == nxt and not squote:
			skipnext = True
			result.append(prev)
		else:
			result.append(this)
	result = ''.join(result)
	print('%s # bang-bang count = %i' % (result, result.count('!!')))
	readline.add_history(result)
	prev = result
