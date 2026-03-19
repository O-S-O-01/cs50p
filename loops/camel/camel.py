variable= input('what is the name of your variable in camelCase?')
#initialize an empty string for snake case 
snake_case=""
for v in variable:
	if v.isupper():
		snake_case += "_" + v.lower()
	else:
		snake_case  += v
print(snake_case)
