coke_price= 50
while coke_price > 0:
	coin=int(input('Insert Coin: '))
	if coin in [25, 10, 5]:
		coke_price -= coin
		if coke_price > 0:
			print(f'Amount Due: {coke_price}') 
	else:
		print(f'Invalid coin. Amount Due: {coke_price}')
print(f'Change Owed: {abs(coke_price)}')