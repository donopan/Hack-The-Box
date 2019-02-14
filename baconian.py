'''This is a Baconian Cipher/Decipher
'''
Dictionary = {'A':'AAAAA','B':'AAAAN','C':'AAANA','D':'AAANN','E':'AANAA','F':'AANAN','G':'AANNA','H':'AANNN','I':'ANAAA','K':'ANAAN','L':'ANANA','M':'ANANN','N':'ANNAA','O':'ANNAN','P':'ANNNA','Q':'ANNNN','R':'NAAAA','S':'NAAAN','T':'NAANA','U':'NAANN','W':'NANAA','X':'NANAN','Y':'NANNA','Z':'NANNN'}

batman=open("finale.txt")
cadena=""
splitcadena=[]
for i in batman:
	cadena+=i
print(len(cadena))

def chunk_str(str, chunk_size):
	return [str[i:i+chunk_size] for i in range(0, len(str), chunk_size)]

print cadena
splitcadena=chunk_str(cadena,5)
print(splitcadena)

def cipherBaconian(mcla, dictionary):
	Cipher=""
	for i in mcla:
		if i in dictionary:
			Cipher+=dictionary[i]
		else:
			continue
	return Cipher

def decipherBaconian(mcifrado, dictionary):
	Decipher=""	
	mcifrado = chunk_str(mcifrado,5)
	for i in mcifrado:
		for j in dictionary:
			print j
			if i == dictionary[j]:
				Decipher+= j
			else:
				continue	
	return Decipher

cifrado = cipherBaconian("HOLA",Dictionary)
print (cifrado)

decifrado = decipherBaconian(cadena,Dictionary)
print (decifrado)


