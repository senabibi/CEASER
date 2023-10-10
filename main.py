from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
	
	
	def encrypt(text,shift):
		en=""
		for letter in text:
			position=shift+alphabet.index(letter)
			if position>len(alphabet):
				position=position-len(alphabet)
				new_letter=alphabet[position]
				en+=new_letter
			else:
				new_letter=alphabet[position]
				en+=new_letter
		print(en)
	def decrypt(text,shift):
		de=""
		for letter in text:
			position=alphabet.index(letter)-shift
			new_letter=alphabet[position]
			de+=new_letter
		print(de)
	
	if direction=="decode":
		decrypt(text,shift)
	else:
		encrypt(text,shift)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
		
caesar(text,shift,direction)
