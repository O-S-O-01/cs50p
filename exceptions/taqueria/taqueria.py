def main():
	meal_menu = { "Baja Taco": 4.25, "Burrito": 7.50,
			 "Bowl": 8.50,  "Nachos": 11.00,    
			 "Quesadilla": 8.50, "Super Burrito": 8.50,   
			  "Super Quesadilla": 9.50,"Taco": 3.00,    	
			 "Tortilla Salad": 8.00
		 } 
	total=0
	while True:
		try:
			item=input('what meal do you want: ' ).title()
			if item in meal_menu:
				total +=meal_menu[item]
				print(f'${total:.2f}')
			else:
				print('not in menu')
		except EOFError:
				print('\nthank you for your patronage...')
				break
if __name__ =='__main__':
	main()
