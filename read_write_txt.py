f = open('texto.txt', 'r')

# Read the file
print(f.read())

# Close the file
f.close()

# Open the file in write mode
f = open('texto.txt', 'w')

texto = ['En un lugar de la Mancha\n', 'de cuyo nombre no quiero acordarme']

f.writelines(texto)

f.close()
