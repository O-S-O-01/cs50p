life_question =  input('what is the answer to the great question of life, the universe and everything?')
answer= life_question.strip().lower()

if answer == '42' or answer == 'forty-two' or answer == 'forty two':
	print ('yes')
else:
	print('no')
 