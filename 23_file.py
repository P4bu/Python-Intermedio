file = open('./text.txt')
#print(file.read()) # Lee todo el archivo
#print(file.readline()) # Lee linea a linea como los iteradores

for line in file:
    print(line)

file.close() # Para cerrar el archivo

with open('./text.txt') as file: # Cierra el archivo automaticamente
    for line in file:
        print(line)


