greetings= input ('goodmorning banker....: ')
greeting = greetings.strip().lower()

if greeting.startswith('hello'):
	print('$0')
elif greeting.startswith('h'):
	print('$20')
else:
	print('$100')

