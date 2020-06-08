# Open output.txt as a text file for writing
stream = open('output.txt', 'wt')

print('\nCan I write to this file? ' + str(stream.writable()) + '\n')

# Write a single string 
stream.write('H') 
# Write one or more strings
stream.writelines(['ello',' ','world']) 
# Write a new line
stream.write('\n') 

names = ['Susan','Christopher']
stream.writelines(names)

# Here's a neat trick to insert a new line between items in the list
# Write a new line
stream.write('\n')  
stream.writelines('\n'.join(names))
# Flush stream and close
stream.close() 
