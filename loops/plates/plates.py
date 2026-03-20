def main():
	plate = input ('plate: ').strip()
	if is_valid(plate):
		print('valid')
	else:
		print('invalid')

def is_valid(plate):
	if len(plate) < 2 or len(plate) > 6:
		return False
	if not plate[0].isalpha() or not plate[1].isalpha():
		return False
	if not plate.isalnum():
		return False
	number_started =False
	for char in plate:
		if char.isdigit():
			if not number_started:
				number_started = True
				if char == '0':
					return False
		else:
			if number_started:
				return False
	return True
main()
