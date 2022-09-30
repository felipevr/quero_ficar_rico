
word = 'nadia'
frase = 'the porcupine wears a green necklace'

def main():
	p = 0
	s = len(word)
	f = ''
	for l in frase:
		if l != ' ':
			int  = vai(word[p])
			int = cifra(vai(l), int)
			l = volta(int)
			p += 1
			p = p % s
		f += l
		print(l)
	print(f)
	print('FIM!')
	
def vai(letra):
	return ord(letra) - ord('a')
	
def volta(int):
	return chr(int + ord('a'))
	
def cifra(int, p):
	return (int + p) % 26
	
def decifra(int, p):
	return (int - p) % 26
	
main()