set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# union "|" suma los elementos de estos sin repetir elementos 
set_c = set_a.union(set_b)
print(set_c)

# intersection "&" toma unicamente los elementos que son en comun
set_d = set_a.intersection(set_b)
print(set_d)

# difference "-" resta los elementos del segundo conjunto al primero
set_e = set_a.difference(set_b)
print(set_e)

# symmtric_difference "^" La diferencia simetrica entre dos conjutnos consta de restar todos los elementos de ambos exceptuando el elemento en común
set_f = set_a.symmetric_difference(set_b)
print(set_f)
