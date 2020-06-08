try:
	stream = open('output.txt', 'wt')
	stream.write('Lorem ipsum dolar')
finally:
	# THIS IS REALLY IMPORTANT!!
	stream.close() 

# With open('output.txt', 'wt') as stream:
# 	stream.write('Lorem ipsum dolar')
