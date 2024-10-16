import sys
print(sys.path)

import re # Expresiones regulares
text = 'Mi numero de telefono es 333 222 111, el codigo del pais es 57, mi numoer de la suerte es 10'
result = re.findall('[0-9]+', text)
print(result)

import time # Horas y fechas
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections # Para manejar listas
numbers = [1,1,2,3,4,4,5,6,5,4]
counter = collections.Counter(numbers)
print(counter)
