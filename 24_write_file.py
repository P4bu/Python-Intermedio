with open('./text.txt', 'r+') as file: # Cierra el archivo automaticamente 'r+= lectura y escritura 
    for line in file:
        print(line)
    file.write('Nuevas cosas en este archivo\n')
    file.write('Nuevas cosas en este archivo\n')
    file.write('Nuevas cosas en este archivo\n')


