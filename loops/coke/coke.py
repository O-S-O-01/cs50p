coke_price= 50
while coke_price > 0:
	coin=int(input('please insert coin: '))
	if coin in [25, 10, 5]:
		coke_price -= coin
		if coke_price > 0:
			print(f'amount due:{coke_price}') 
	else:
		print(f'invalid coin use 25, 10, 5, amount due:{coke_price} ')
print(f'change owed: {abs(coke_price)}')

