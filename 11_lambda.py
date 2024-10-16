def increment(x):
    return x + 1

increment_2 = lambda x: x + 1

result = increment(3)
print(result)

result = increment_2(20)
print(result)

full_name = lambda name, last_name: f'My name is {name.title()} {last_name.title()}'
text = full_name('Pablo', 'Barra Urtubia')
print(text)