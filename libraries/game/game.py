def main():
	import random
	while True:
		try:
			level = int(input('Level: '))
			if level > 0:
				break
# we use except valueerror here because 'input' accept only strings, so if a string is typed we get a value error becaue of the int tag on line four  
		except ValueError:
			continue

	number = random.randint (1, level)

	while True:
		try:
			guess = int(input('Guess: '))
		except ValueError:
			continue

		if guess < 1:
			continue

		if guess < number:				
			print ('Too small!')
		elif guess > number:
			print ('Too large!')
		else:
			print('Just right!')
			break

	
if __name__=='__main__':
	main()
