def main():
	from pyfiglet import Figlet
	import sys 
	import random
	figlet=Figlet()
	fonts=figlet.getFonts()

	if len(sys.argv) ==1:
		font=random.choice(fonts)
	elif len(sys.argv) ==3:
		if sys.argv[1] not in ['-f', '--font']:
			sys.exit('invalid usage')
		if sys.argv[2] not in fonts:
			sys.exit('invalid font')
		font=sys.argv[2]
	else:
		sys.exit('invalid usage')

	figlet.setFont(font=font)

	text=input('input: ')
	print(figlet.renderText(text))
if __name__=='__main__':
	main()
