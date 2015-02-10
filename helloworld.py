
while True:

	i = 0
	i = int(raw_input("Enter a number:"))
	
	try:
		if i == 1:
			print('Hello World {0}'.format(i))
		elif i == 2:
			print('Too two {0}'.format(i))
		else:
			print('No way')
	except ValueError:
		print 'not a number'
