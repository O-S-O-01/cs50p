text = input('what is your message? ' )
result=''
for t in text:
	if t.lower() not in ['a', 'e', 'i', 'o', 'u' ]:
		result += t
print (result)
