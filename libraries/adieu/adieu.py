def main():
	import inflect
	p =inflect.engine()
	
	names = []
	while True:
		try:
			name =input('Name: ')
			names.append(name)
		except EOFError:
			break
	outcome= p.join(names)
	print(f'Adieu, adieu, to {outcome}')
if __name__ == '__main__':
	main()
