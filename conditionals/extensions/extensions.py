program = input ('what is the name of the file? ')
programs=program.strip().lower()
if programs.endswith('.gif'):
	print ('image/gif')
elif programs.endswith('.jpg') or programs.endswith('.jpeg'):
	print('image/jpeg')
elif programs.endswith('.png'):
	print ('image/png')
elif programs.endswith('.txt'):
	print ('text/plain')
elif programs.endswith('.pdf'):
	print ('application/pdf')
elif programs.endswith('.zip'):
	print('applications/zip')
else:
	print('application/octet-stream')
