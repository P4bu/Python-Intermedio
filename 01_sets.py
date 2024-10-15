# Conjuntos 
# Los conjuntos no acepta los elementos duplicados
set_countries = {'col', 'mex', 'bol', 'col'}
print(set_countries)

print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tupla = set(('abc', 'cvb', 'as', 'abc'))
print(set_from_tupla)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)